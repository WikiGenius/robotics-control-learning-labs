# Lab 01: LQR Double Integrator

This starter lab gives the repository one small runnable public example.

## Purpose

The lab uses a discrete double-integrator model as a clean baseline for state-space feedback control. It is not a private research experiment and does not represent unpublished mobile-manipulator control work.

## Model

State:

```text
x = [position, velocity]^T
```

Input:

```text
u = acceleration-like control command
```

The script discretizes the model with a small timestep and computes an infinite-horizon discrete LQR gain using Riccati iteration.

## Run

From the repository root:

```bash
python scripts/lqr_double_integrator.py
```

The script always writes:

```text
results/lqr_double_integrator_summary.csv
```

If `matplotlib` is installed, it also writes:

```text
media/lqr_double_integrator.png
```

## Why This Belongs Here

The example establishes the structure for future labs:

1. define a simple model,
2. choose costs,
3. solve for a controller,
4. simulate closed-loop behavior,
5. save results and optional media,
6. state what is simplified.

Future labs can extend this pattern to observers, trajectory tracking, and simplified mobile-manipulator examples.

## Limitations

- Toy double-integrator dynamics only.
- No actuator limits, noise, or model uncertainty.
- No ROS2 or mobile-manipulator integration.
- Intended as a public baseline pattern, not a research claim.
