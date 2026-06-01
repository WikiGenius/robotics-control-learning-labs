"""Minimal public LQR lab for a discrete double-integrator model.

This is a small, reproducible baseline example. It is intentionally separate
from private research experiments and uses a toy system with synthetic data.
"""

from pathlib import Path

import numpy as np

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:  # Plotting is helpful but not required for the CSV result.
    plt = None


def solve_discrete_lqr(A: np.ndarray, B: np.ndarray, Q: np.ndarray, R: np.ndarray, iterations: int = 500) -> np.ndarray:
    """Solve a discrete-time infinite-horizon LQR problem by Riccati iteration."""
    P = Q.copy()
    for _ in range(iterations):
        gain_term = R + B.T @ P @ B
        K = np.linalg.solve(gain_term, B.T @ P @ A)
        P = Q + A.T @ P @ (A - B @ K)
    return K


def simulate(A: np.ndarray, B: np.ndarray, K: np.ndarray, x0: np.ndarray, steps: int) -> tuple[np.ndarray, np.ndarray]:
    states = np.zeros((steps + 1, A.shape[0]))
    controls = np.zeros(steps)
    states[0] = x0

    for k in range(steps):
        u = float((-K @ states[k]).item())
        controls[k] = u
        states[k + 1] = A @ states[k] + B.flatten() * u

    return states, controls


def write_plot(media_dir: Path, time: np.ndarray, control_time: np.ndarray, states: np.ndarray, controls: np.ndarray) -> bool:
    if plt is None:
        return False

    fig, (ax_state, ax_control) = plt.subplots(2, 1, figsize=(8, 6), sharex=False)
    ax_state.plot(time, states[:, 0], label="position")
    ax_state.plot(time, states[:, 1], label="velocity")
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
    A = np.array([[1.0, dt], [0.0, 1.0]])
    B = np.array([[0.5 * dt * dt], [dt]])
    Q = np.diag([10.0, 1.0])
    R = np.array([[0.1]])

    K = solve_discrete_lqr(A, B, Q, R)
    states, controls = simulate(A, B, K, x0=np.array([1.0, 0.0]), steps=160)

    repo_root = Path(__file__).resolve().parents[1]
    results_dir = repo_root / "results"
    media_dir = repo_root / "media"
    results_dir.mkdir(exist_ok=True)
    media_dir.mkdir(exist_ok=True)

    time = np.arange(states.shape[0]) * dt
    control_time = np.arange(controls.shape[0]) * dt

    summary = np.column_stack(
        [
            time,
            states[:, 0],
            states[:, 1],
            np.r_[controls, np.nan],
        ]
    )
    np.savetxt(
        results_dir / "lqr_double_integrator_summary.csv",
        summary,
        delimiter=",",
        header="time_s,position_m,velocity_m_per_s,control_input",
        comments="",
    )

    wrote_plot = write_plot(media_dir, time, control_time, states, controls)

    print("LQR gain K:", np.array2string(K, precision=4))
    print("Final state:", np.array2string(states[-1], precision=4))
    print("Wrote results/lqr_double_integrator_summary.csv")
    if wrote_plot:
        print("Wrote media/lqr_double_integrator.png")
    else:
        print("Skipped plot because matplotlib is not installed")


if __name__ == "__main__":
    main()
