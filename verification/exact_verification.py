#!/usr/bin/env python3
"""Exact finite checks for the Luce choice-event covariance theorems."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations
from typing import Iterable, Iterator, Sequence


@dataclass(frozen=True)
class Event:
    scope: frozenset[int]
    pivot: int


def weight(scope: Iterable[int], rates: Sequence[int]) -> int:
    return sum(rates[item] for item in scope)


def all_events(item_count: int) -> list[Event]:
    events: list[Event] = []
    items = range(item_count)
    for size in range(2, item_count + 1):
        for scope_tuple in combinations(items, size):
            scope = frozenset(scope_tuple)
            events.extend(Event(scope, pivot) for pivot in scope_tuple)
    return events


def event_key(event: Event) -> tuple[int, tuple[int, ...], int]:
    return len(event.scope), tuple(sorted(event.scope)), event.pivot


def ranking_probability(order: Sequence[int], rates: Sequence[int]) -> Fraction:
    remaining_rate = sum(rates)
    probability = Fraction(1)
    for item in order:
        probability *= Fraction(rates[item], remaining_rate)
        remaining_rate -= rates[item]
    return probability


def event_holds(order: Sequence[int], event: Event) -> bool:
    position = {item: index for index, item in enumerate(order)}
    return all(position[event.pivot] < position[item] for item in event.scope if item != event.pivot)


def distribution(rates: Sequence[int]) -> list[tuple[tuple[int, ...], Fraction]]:
    assert rates and all(rate > 0 for rate in rates)
    ranked_distribution = [
        (order, ranking_probability(order, rates))
        for order in permutations(range(len(rates)))
    ]
    assert sum((mass for _, mass in ranked_distribution), start=Fraction(0)) == 1
    return ranked_distribution


def probability(
    events: Sequence[Event],
    ranked_distribution: Sequence[tuple[tuple[int, ...], Fraction]],
) -> Fraction:
    return sum(
        (mass for order, mass in ranked_distribution if all(event_holds(order, event) for event in events)),
        start=Fraction(0),
    )


def marginal(event: Event, rates: Sequence[int]) -> Fraction:
    return Fraction(rates[event.pivot], weight(event.scope, rates))


def formula_covariance(first: Event, second: Event, rates: Sequence[int]) -> Fraction:
    scope_s, a = first.scope, first.pivot
    scope_t, b = second.scope, second.pivot
    union = scope_s | scope_t
    lambda_s = weight(scope_s, rates)
    lambda_t = weight(scope_t, rates)
    lambda_u = weight(union, rates)
    alpha = rates[a]
    beta = rates[b]

    if a == b:
        common_other = weight((scope_s & scope_t) - {a}, rates)
        only_s = weight(scope_s - scope_t, rates)
        only_t = weight(scope_t - scope_s, rates)
        numerator = alpha * (common_other * lambda_u + only_s * only_t)
        return Fraction(numerator, lambda_s * lambda_t * lambda_u)

    a_crosses = a in scope_t
    b_crosses = b in scope_s
    if not a_crosses and not b_crosses:
        numerator = alpha * beta * weight(scope_s & scope_t, rates)
        return Fraction(numerator, lambda_s * lambda_t * lambda_u)
    if a_crosses and not b_crosses:
        numerator = -alpha * beta * weight(scope_s - scope_t, rates)
        return Fraction(numerator, lambda_s * lambda_t * lambda_u)
    if b_crosses and not a_crosses:
        numerator = -alpha * beta * weight(scope_t - scope_s, rates)
        return Fraction(numerator, lambda_s * lambda_t * lambda_u)
    return -Fraction(alpha * beta, lambda_s * lambda_t)


def pivot_laminar(first: Event, second: Event) -> bool:
    scope_s, scope_t = first.scope, second.scope
    if scope_s.isdisjoint(scope_t):
        return True
    if scope_s < scope_t:
        return second.pivot not in scope_s
    if scope_t < scope_s:
        return first.pivot not in scope_t
    return False


def verify_pair_formulas(rates: Sequence[int]) -> int:
    events = all_events(len(rates))
    ranked_distribution = distribution(rates)
    checked = 0
    for first, second in combinations_with_replacement(events, 2):
        actual = probability((first, second), ranked_distribution)
        actual -= marginal(first, rates) * marginal(second, rates)
        expected = formula_covariance(first, second, rates)
        assert actual == expected, (first, second, actual, expected)
        assert (actual == 0) == pivot_laminar(first, second), (first, second, actual)
        checked += 1
    return checked


def maximal_cliques(events: Sequence[Event]) -> Iterator[tuple[Event, ...]]:
    adjacency = {
        event: {other for other in events if other != event and pivot_laminar(event, other)}
        for event in events
    }

    def visit(
        chosen: set[Event],
        candidates: set[Event],
        excluded: set[Event],
    ) -> Iterator[tuple[Event, ...]]:
        if not candidates and not excluded:
            yield tuple(sorted(chosen, key=event_key))
            return
        pivot = max(candidates | excluded, key=lambda event: len(candidates & adjacency[event]), default=None)
        branch_vertices = candidates - (adjacency[pivot] if pivot is not None else set())
        for event in tuple(branch_vertices):
            yield from visit(
                chosen | {event},
                candidates & adjacency[event],
                excluded & adjacency[event],
            )
            candidates.remove(event)
            excluded.add(event)

    yield from visit(set(), set(events), set())


def maximal_scope_count(family: Sequence[Event]) -> int:
    scopes = {event.scope for event in family}
    return sum(not any(scope < other for other in scopes) for scope in scopes)


def is_full_flag_union(family: Sequence[Event]) -> bool:
    maximal_scopes = [
        event.scope
        for event in family
        if not any(event.scope < other.scope for other in family)
    ]
    if len(set(maximal_scopes)) != len(maximal_scopes):
        return False
    for root in maximal_scopes:
        component = sorted(
            (event for event in family if event.scope <= root),
            key=lambda event: len(event.scope),
        )
        if len(component) != len(root) - 1:
            return False
        if [len(event.scope) for event in component] != list(range(2, len(root) + 1)):
            return False
        for smaller, larger in zip(component, component[1:]):
            if not smaller.scope < larger.scope:
                return False
            if larger.pivot not in larger.scope - smaller.scope:
                return False
    return True


def verify_independence_collapse(rates: Sequence[int]) -> int:
    events = all_events(len(rates))
    ranked_distribution = distribution(rates)
    clique_count = 0
    for clique in maximal_cliques(events):
        clique_count += 1
        for size in range(2, len(clique) + 1):
            for family in combinations(clique, size):
                actual = probability(family, ranked_distribution)
                expected = Fraction(1)
                for event in family:
                    expected *= marginal(event, rates)
                assert actual == expected, (family, actual, expected)
                used_items = frozenset().union(*(event.scope for event in family))
                roots = maximal_scope_count(family)
                assert len(family) <= len(used_items) - roots, family
                if len(family) == len(used_items) - roots:
                    assert is_full_flag_union(family), family
    return clique_count


def main() -> None:
    pair_checks = 0
    for rates in ((1, 1, 1, 1), (1, 2, 3, 5), (2, 3, 5, 7, 11)):
        pair_checks += verify_pair_formulas(rates)
    clique_checks = verify_independence_collapse((1, 2, 3, 5))
    print(f"exact pair checks: {pair_checks}")
    print(f"maximal independent families checked: {clique_checks}")


if __name__ == "__main__":
    main()
