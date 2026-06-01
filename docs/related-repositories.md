# Related Repositories

This page explains how the control repositories fit together.

## Public Control Family

| Repo | Role | Why it matters |
|---|---|---|
| [`robotics-control-learning-labs`](https://github.com/WikiGenius/robotics-control-learning-labs) | Public control hub | Organizes state-space, LQR, observers, and reproducible control labs. |
| [`wmm-trajectory-tracking`](https://github.com/WikiGenius/wmm-trajectory-tracking) | Whole-body trajectory tracking | Connects control to mobile-manipulator motion and scan execution. |
| [`Cruise_control`](https://github.com/WikiGenius/Cruise_control) | MATLAB/Simulink control exercise | Shows classical control modeling and simulation practice. |
| [`RoboticScrewTheoryToolkit`](https://github.com/WikiGenius/RoboticScrewTheoryToolkit) | Robot math toolkit | Supports kinematics, Jacobians, screw theory, and manipulator modeling. |
| [`3dof-robot-arm-report`](https://github.com/WikiGenius/3dof-robot-arm-report) | Technical report | Preserves modeling/control write-up evidence in a clean artifact. |

## Private Companion Layer

Unpublished control experiments, inverted-pendulum studies, parameter sweeps, and paper-specific uncertainty-aware control code should remain private.

When a private experiment becomes safe to show publicly, release only a distilled version here:

1. Use synthetic or non-sensitive data.
2. Remove unpublished algorithm details that belong in a paper first.
3. Include a short model derivation or citation.
4. Add reproducible commands.
5. Add plots under `results/` and figures or GIFs under `media/`.
6. State what was simplified.

## Connection to Main Research

The control family supports structure-aware mobile manipulation by providing:

- stable base-arm trajectory tracking,
- LQR/observer baselines for comparison,
- state-space modeling practice,
- kinematic foundations for arm motion,
- experiment logs and metrics that can later connect to active scanning.

The downstream public demo is [`line-scan-mobile-manipulator-demo`](https://github.com/WikiGenius/line-scan-mobile-manipulator-demo). That repo should eventually consume simplified controllers or metrics from this control family.
