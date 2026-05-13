# Core Architecture

The project argues for a shift from a single-agent operating model to a
constitutional runtime.

## Problem

Single-agent workflows can be productive for short tasks, but they become
unstable when long-horizon work depends on implicit memory, informal authority,
unbounded tool use, and conversational definitions of done.

The failure is not only model error. It is the absence of runtime governance.

## Runtime Primitives

- Mission kernel: preserves durable user intent outside any one agent session.
- Task registry: gives work units identity, scope, owner, status, and closure
  requirements.
- Authority manager: grants scoped capabilities by actor, task, artifact,
  action class, environment, and duration.
- Policy engine: evaluates whether an actor may perform an action.
- Tool broker: routes tool calls through policy and audit controls.
- Audit log: records decisions, actions, evidence, authority context, and
  affected artifacts.
- Memory substrate: stores useful state with provenance instead of treating
  memory as ungrounded recall.
- Delegation protocol: transfers work through explicit contracts and reviewable
  handoff artifacts.
- Closure protocol: requires evidence, residual risk notes, and acceptance
  criteria before a task is considered complete.

## Design Principle

Agents are governed actors. They are not the whole operating system.

The runtime is responsible for the durable rules: who owns the task, what
authority exists, what evidence is required, what changed, and when closure is
legitimate.
