"""Minimal public LQR lab for a discrete double-integrator model.

This is a small, reproducible baseline example. It is intentionally separate
from private research experiments and uses a toy system with synthetic data.
The core CSV output uses only the Python standard library.
"""

from __future__ import annotations

import csv
from pathlib import Path

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:  # Plotting is helpful but not required for the CSV result.
    plt = None

Matrix = list[list[float]]
Vector = list[float]


def matmul(A: Matrix, B: Matrix) -> Matrix:
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def transpose(A: Matrix) -> Matrix:
    return [list(row) for row in zip(*A)]


def matadd(A: Matrix, B: Matrix) -> Matrix:
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matsub(A: Matrix, B: Matrix) -> Matrix:
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def outer_column_row(B: Matrix, K: Matrix) -> Matrix:
    return [[B[i][0] * K[0][j] for j in range(len(K[0]))] for i in range(len(B))]


def solve_discrete_lqr(A: Matrix, B: Matrix, Q: Matrix, R: Matrix, iterations: int = 500) -> Matrix:
    """Solve a 2-state, 1-input discrete LQR problem by Riccati iteration."""
    P = [row[:] for row in Q]
    At = transpose(A)
    Bt = transpose(B)

    for _ in range(iterations):
        BtP = matmul(Bt, P)
        gain_denominator = R[0][0] + matmul(BtP, B)[0][0]
        gain_numerator = matmul(BtP, A)[0]
        K = [[value / gain_denominator for value in gain_numerator]]
        P = matadd(Q, matmul(matmul(At, P), matsub(A, outer_column_row(B, K))))

    return K


def matvec(A: Matrix, x: Vector) -> Vector:
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]


def simulate(A: Matrix, B: Matrix, K: Matrix, x0: Vector, steps: int) -> tuple[list[Vector], Vector]:
    states = [x0[:]]
    controls: Vector = []

    for _ in range(steps):
        current = states[-1]
        u = -(K[0][0] * current[0] + K[0][1] * current[1])
        controls.append(u)
        ax = matvec(A, current)
        states.append([ax[i] + B[i][0] * u for i in range(len(ax))])

    return states, controls


def write_csv(results_dir: Path, dt: float, states: list[Vector], controls: Vector) -> None:
    with (results_dir / "lqr_double_integrator_summary.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["time_s", "position_m", "velocity_m_per_s", "control_input"])
        for idx, state in enumerate(states):
            control = controls[idx] if idx < len(controls) else ""
            writer.writerow([round(idx * dt, 6), state[0], state[1], control])


def write_plot(media_dir: Path, dt: float, states: list[Vector], controls: Vector) -> bool:
    if plt is None:
        return False

    time = [idx * dt for idx in range(len(states))]
    control_time = [idx * dt for idx in range(len(controls))]
    positions = [state[0] for state in states]
    velocities = [state[1] for state in states]

    fig, (ax_state, ax_control) = plt.subplots(2, 1, figsize=(8, 6), sharex=False)
    ax_state.plot(time, positions, label="position")
    ax_state.plot(time, velocities, label="velocity")
    ax_state.set_ylabel("state")
    ax_state.grid(True, alpha=0.3)
    ax_state.legend(loc="best")

    ax_control.plot(control_time, controls, color="tab:red", label="control")
    ax_control.set_xlabel("time [s]")
    ax_control.set_ylabel("input")
    ax_control.grid(True, alpha=0.3)
    ax_control.legend(loc="best")

    fig.tight_layout()
    fig.savefig(media_dir / "lqr_double_integrator.png", dpi=160)
    return True


def main() -> None:
    dt = 0.05
    A = [[1.0, dt], [0.0, 1.0]]
    B = [[0.5 * dt * dt], [dt]]
    Q = [[10.0, 0.0], [0.0, 1.0]]
    R = [[0.1]]

    K = solve_discrete_lqr(A, B, Q, R)
    states, controls = simulate(A, B, K, x0=[1.0, 0.0], steps=160)

    repo_root = Path(__file__).resolve().parents[1]
    results_dir = repo_root / "results"
    media_dir = repo_root / "media"
    results_dir.mkdir(exist_ok=True)
    media_dir.mkdir(exist_ok=True)

    write_csv(results_dir, dt, states, controls)
    wrote_plot = write_plot(media_dir, dt, states, controls)

    print("LQR gain K: [[{:.4f}, {:.4f}]]".format(K[0][0], K[0][1]))
    print("Final state: [{:.4f}, {:.4f}]".format(states[-1][0], states[-1][1]))
    print("Wrote results/lqr_double_integrator_summary.csv")
    if wrote_plot:
        print("Wrote media/lqr_double_integrator.png")
    else:
        print("Skipped plot because matplotlib is not installed")


if __name__ == "__main__":
    main()
