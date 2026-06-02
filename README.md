# Robotics Control Learning Labs

Public control-foundation hub for reproducible robotics/control learning artifacts, including state-space modeling, LQR, observers, trajectory tracking, and MATLAB/Simulink workflows.

## Purpose

This repository exists to organize public-safe control examples that support my robotics research portfolio without exposing unpublished PhD control experiments, advisor notes, paper drafts, or private ablations.

It is the broad pinned control hub. Focused public support repos, such as [`ipendulum`](https://github.com/WikiGenius/ipendulum), sit under this hub as concrete examples.

## Relation to My PhD Direction

My research direction requires planning and control for mobile manipulation under sensing, geometry, and uncertainty constraints. This repo supports that direction by organizing:

- state-space modeling practice,
- LQR and feedback-control baselines,
- observer/state-estimation examples,
- trajectory-tracking foundations,
- MATLAB/Simulink and Python analysis patterns,
- public control examples that can later connect to active scanning.

Related public repos:

| Related repo | Public role |
|---|---|
| [`ipendulum`](https://github.com/WikiGenius/ipendulum) | Inverted-pendulum MATLAB/Simulink lab with PID, LQR, pole placement, observers, LQG, and demo animations. |
| [`wmm-trajectory-tracking`](https://github.com/WikiGenius/wmm-trajectory-tracking) | Whole-body mobile-manipulator trajectory tracking and control support. |
| [`Cruise_control`](https://github.com/WikiGenius/Cruise_control) | MATLAB/Simulink control exercise and energy/control artifact. |
| [`RoboticScrewTheoryToolkit`](https://github.com/WikiGenius/RoboticScrewTheoryToolkit) | Kinematics, screw theory, Jacobians, and robot math foundations. |
| [`line-scan-mobile-manipulator-demo`](https://github.com/WikiGenius/line-scan-mobile-manipulator-demo) | Downstream active-scanning scaffold that will need planning/control foundations. |

Archived report artifacts, such as `3dof-robot-arm-report`, remain available as history but are not part of the active control portfolio.

## Maturity Level

**Current status:** Public research scaffold / early-stage organization repo with one runnable starter lab

This repository is currently intended to organize the public-facing control structure and host simplified, non-confidential demos. It does not yet represent a complete control library or a validated robot controller.

### Implemented now

- [x] Repository structure
- [x] README and project organization
- [x] Public related-repository map
- [x] Minimal LQR toy demo
- [x] CSV output from the LQR starter script
- [x] Link to public inverted-pendulum control support repo
- [ ] Observer lab in this repo
- [ ] MATLAB/Simulink lab collection in this repo
- [ ] Mobile-manipulator tracking comparison
- [ ] Paper-supporting implementation

### Not included publicly

- Unpublished research algorithm
- Private paper draft
- Advisor/collaborator notes
- Real lab data
- Full ablation studies
- Confidential experiment results
- Paper-specific uncertainty-aware control code

## Current Contents

```text
docs/       related-repository map and starter lab note
scripts/    minimal LQR double-integrator starter script
results/    CSV outputs from public-safe demos
media/      optional plots/GIFs when generated
src/        future reusable control code
```

## What This Repo Demonstrates Now

This repo currently demonstrates:

- a clean public hub for control-learning artifacts,
- a dependency-free LQR double-integrator starter example,
- an output pattern for saving public-safe result tables,
- how focused support repos such as `ipendulum` fit under the control family.

The starter LQR example is a toy baseline. It is not a robot controller and does not represent a publishable control method.

## Planned Development Roadmap

- **Stage 0: repository scaffold** - organize README, folders, related repos, and public/private policy.
- **Stage 1: toy synthetic example** - maintain the double-integrator LQR starter lab.
- **Stage 2: metric computation** - add tracking error, control effort, and settling-time metrics.
- **Stage 3: baseline controllers** - add observer and feedback-control examples.
- **Stage 4: robotics connection** - connect examples to trajectory tracking and mobile-manipulator scanning needs.
- **Stage 5: experiment logging and plots** - add public CSV/plot outputs.
- **Stage 6: paper-supporting private implementation** - keep unpublished methods private.
- **Stage 7: post-publication public release** - release sanitized code/results after approval.

## Public / Private Boundary

Public here:

- simplified examples,
- toy systems,
- public control baselines,
- reproducible commands,
- non-confidential plots/tables,
- links to public support repos.

Private elsewhere:

- unpublished control methods,
- advisor notes,
- paper drafts,
- internal ablations,
- private parameter sweeps,
- uncertainty-aware control experiments not ready for release.

## How to Run

Run the current starter lab:

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

## Expected Future Outputs

Future public artifacts may include:

- step-response plots,
- tracking-error tables,
- control-effort summaries,
- observer convergence plots,
- Simulink screenshots,
- public technical notes.

## Limitations

This repository is currently an early-stage public control scaffold. It does not yet include:

- a full control curriculum,
- a validated robot controller,
- a mobile-manipulator tracking benchmark,
- complete observer labs,
- paper-level results.

MATLAB/Simulink examples may require licensed toolboxes.

## Citation / Acknowledgment

Acknowledge any textbook, course, paper, MATLAB example, Python library, or robotics/control framework used in each lab. Third-party materials remain under their own licenses.

## Rights and Reuse

This repository is shared as a public academic portfolio/scaffold. Unless a separate open-source license is explicitly added, all rights are reserved by the author.

## Related Organization

See [`docs/related-repositories.md`](docs/related-repositories.md) for how the control repositories fit into the public/private research structure.
