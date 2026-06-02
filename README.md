# Robotics Control Learning Labs

Public control-foundation hub for organizing robotics/control learning artifacts, including state-space modeling, LQR, observers, trajectory tracking, and MATLAB/Simulink workflows.

## Purpose

This repository exists to organize public-safe control foundations that support my robotics research portfolio without exposing unpublished PhD control experiments, advisor notes, paper drafts, or private ablations.

It is the broad pinned control hub. Focused public support repos, such as [`ipendulum`](https://github.com/WikiGenius/ipendulum), sit under this hub as concrete examples of learning control on specific systems.

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

## Maturity Level

**Current status:** Public research organization repo / control-family hub

This repository is currently intended to organize the public-facing control structure and connect related control repos. It does not currently contain a runnable in-repo lab script, complete control library, or validated robot controller.

### Implemented now

- [x] Repository structure
- [x] README and project organization
- [x] Public related-repository map
- [x] Link to public inverted-pendulum control support repo
- [x] Link to mobile-manipulator trajectory-tracking support repo
- [ ] In-repo public-safe LQR lab
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
docs/       related-repository map and control-family notes
scripts/    reserved for future public-safe scripts
results/    reserved for future public-safe result tables
media/      reserved for future plots/GIFs/screenshots
src/        reserved for future reusable control code
```

## What This Repo Demonstrates Now

This repo currently demonstrates:

- a clean public hub for control-learning artifacts,
- how focused support repos such as `ipendulum` fit under the control family,
- how control foundations support mobile manipulation, active scanning, trajectory tracking, and uncertainty-aware planning,
- a public/private boundary for keeping unpublished control research private until release.

## Planned Development Roadmap

- **Stage 0: repository scaffold** - organize README, folders, related repos, and public/private policy.
- **Stage 1: public-safe control lab** - add an intentionally reviewed, simple LQR or observer lab when ready.
- **Stage 2: metric computation** - add tracking error, control effort, and settling-time metrics.
- **Stage 3: baseline controllers** - add observer and feedback-control examples.
- **Stage 4: robotics connection** - connect examples to trajectory tracking and mobile-manipulator scanning needs.
- **Stage 5: experiment logging and plots** - add public CSV/plot outputs.
- **Stage 6: paper-supporting private implementation** - keep unpublished methods private.
- **Stage 7: post-publication public release** - release sanitized code/results after approval.

## Public / Private Boundary

Public here:

- simplified explanations,
- repo organization,
- links to public support repos,
- future public-safe examples,
- non-confidential plots/tables after they are intentionally created.

Private elsewhere:

- unpublished control methods,
- advisor notes,
- paper drafts,
- internal ablations,
- private parameter sweeps,
- uncertainty-aware control experiments not ready for release.

## How to Run

There is currently no runnable in-repo lab script in this public hub.

For concrete public control examples, see [`ipendulum`](https://github.com/WikiGenius/ipendulum) and the other related repos listed above.

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
