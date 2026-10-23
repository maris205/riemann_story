"""Recompute the supplied Fig5 notebook at its original 500,000,000 scale.

Same fixed-u map, binary64 operation order, warm-up and x<0 event rule.
Stream event gaps instead of retaining the notebook's 4 GB trajectory.
Adapted from maris205/prime_logistic, fig5-discrete_gap_spectrum.ipynb,
commit 0bdeaaac9ac3f062e151d27a2d3c50bf241be5ef (Apache-2.0).
The original license is archived in the chapter14 research code directory.
Changes: streaming histogram, compiled recurrence, data export and validation.
Requires numpy and numba. No fast-math or parallel recurrence.
"""
from pathlib import Path
import json
import time
import numpy as np
from numba import njit

HERE = Path(__file__).resolve().parent
U = 1.543689012692076

@njit(fastmath=False)
def chaos_counts(limit, power):
    x = 0.1
    for _ in range(10000):
        x = 1.0 - U * x**power
    counts = np.zeros(512, dtype=np.int64)
    prev = -1
    events = 0
    for i in range(limit):
        x = 1.0 - U * x**power
        if x < 0:
            events += 1
            if prev >= 0:
                gap = i - prev
                if gap >= len(counts):
                    raise ValueError('Increase histogram range')
                counts[gap] += 1
            prev = i
    return counts, events, x

def main():
    # Exact integer histogram check against the literal notebook recurrence.
    x = 0.1
    for _ in range(10000):
        x = 1 - U * x**2
    indices = []
    for i in range(100000):
        x = 1 - U * x**2
        if x < 0:
            indices.append(i)
    check, events, last = chaos_counts(100000, 2.0)
    assert np.array_equal(check, np.bincount(np.diff(indices), minlength=512))
    assert last == x and events == len(indices)
    limit = 500_000_000
    start = time.perf_counter()
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(limit**.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = False
    primes = np.flatnonzero(sieve)
    del sieve
    gaps = np.diff(primes)
    prime_counts = np.bincount(gaps)
    prime_total = len(gaps)
    prime_mean = float(np.mean(gaps))
    del primes, gaps
    print('Prime sieve complete', prime_total + 1, flush=True)
    counts, events, last = chaos_counts(limit, 2.0)
    assert counts.sum() == events - 1
    np.savez_compressed(HERE/'14_wang_gap_data.npz', prime_counts=prime_counts,
                        chaos_counts=counts, limit=limit, u=U,
                        prime_total=prime_total, chaos_total=events-1)
    info = {'limit':limit, 'u':U, 'warmup':10000, 'initial_x':.1,
            'prime_count':prime_total+1, 'chaos_event_count':int(events),
            'prime_mean_gap':prime_mean,
            'chaos_mean_gap':float(counts@np.arange(512)/(events-1)),
            'runtime_seconds':time.perf_counter()-start,
            'validation':'100000-step literal Python histogram and final float matched exactly',
            'model':'autonomous fixed parameter, not the later non-autonomous spectral map'}
    (HERE/'14_wang_gap_metadata.json').write_text(json.dumps(info,indent=2),encoding='utf8')
    print(json.dumps(info), flush=True)

if __name__ == '__main__':
    main()
