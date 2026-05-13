# Chapter 1 Citation Evidence Index

This index maps Chapter 1 claims to the reference evidence package.

It is not a replacement for the final article. It is a citation review aid.

## Current Published References

The final Chapter 1 Markdown currently lists 19 references:

- R1-R7: framing references for agent runtime capability, context engineering, multi-agent orchestration, OpenAI/Hugging Face agent docs, and long-running harnesses
- R8-R10: long-context degradation and long-task capability
- R11-R13: authority, support, delegation, and inter-agent risk
- R14-R15: tool calling and capability governance
- R16: lawful stop and agent autonomy
- R17-R19: closest-neighbor systems and positioning

The local reference matrix primarily supports the empirical sections R1-R16. R17-R19 are positioning references and are not the main focus of this matrix.

## Claim Mapping

### Opening / Framing

Supported by:

- Anthropic, *Building effective agents*
- Anthropic, *Effective context engineering for AI agents*
- OWASP GenAI Security Project, LLM Top 10

Use:

- Define the field-level vocabulary: workflows, agents, context engineering, and excessive agency.
- Keep these citations light. They establish context rather than proving the chapter.

### Section 1.1: Task Ownership Drift

Supported by:

- Liu et al., *Lost in the Middle*, arXiv/ACL/TACL reference: 2307.03172
- Chroma, *Context Rot*
- METR, *Measuring AI Ability to Complete Long Tasks*, arXiv:2503.14499
- LOCA-bench, arXiv:2602.07962
- UltraHorizon, arXiv:2509.21766

Use:

- Support the point that larger context windows do not automatically preserve task identity.
- Avoid claiming these papers directly prove ownership drift; they support the weaker and more defensible claim that long-context reliability degrades and therefore cannot serve as the whole task-identity substrate.

### Section 1.2: Support Quietly Turns Into Ownership

Supported by:

- production failure-mode taxonomies
- CrewAI hierarchical bug reports
- adjacent handoff and scope-creep reports

Use:

- This section is mostly structural reasoning. Use at most one light citation if needed.
- The matrix recommends not over-citing this section.

### Section 1.3: Memory Is Not Evidence

Supported by:

- Anthropic, *Effective context engineering for AI agents*
- AI Hallucination Cases Database
- ACE context collapse, arXiv:2510.04618
- MIRAGE-Bench, arXiv:2507.21017
- When Refusals Fail, arXiv:2512.02445

Use:

- Support the distinction between recall and admissibility.
- The hallucination cases database is a strong concrete example, but should be framed carefully as legal-domain evidence misuse rather than a direct proof of runtime memory architecture.

### Section 1.4: Persona Becomes Authority

Supported by:

- When Personas Override Payoffs, arXiv:2601.10102
- Belief in Authority, arXiv:2601.04790
- Persona-induced bias, arXiv:2511.11789
- Identity drift, arXiv:2412.00804
- CrewAI Issue #2838

Use:

- The strongest insertion is the role identity bias framing plus one engineering bug report.
- Avoid stacking all persona papers into the main article.

### Section 1.5: Delegation Becomes Authorization

Supported by:

- CrewAI Issue #4783
- CrewAI Issue #2054
- CrewAI Issue #3925

Use:

- Treat these as public engineering examples of delegation and authority confusion.
- Do not claim that CrewAI as a project proves the general argument; use the issues as illustrative evidence.

### Section 1.6: Global Chat Becomes Context Pollution

Supported by:

- Anthropic, *How we built our multi-agent research system*
- AutoGen GroupChat bug reports

Use:

- The Anthropic orchestrator-workers design is the positive counterexample.
- AutoGen issues can support the practical failure mode, but the final article can remain concise.

### Section 1.7: Tool Calling Is Not Capability Governance

Supported by:

- OWASP LLM06: Excessive Agency
- MCPTox benchmark cluster
- Breaking MCP Protocol, arXiv:2601.17549
- Prompt Injection Attacks on Agentic Coding Assistants, arXiv:2601.17548

Use:

- This is one of Chapter 1's strongest empirical sections.
- Use OWASP for taxonomy and MCP/tool-poisoning work for measured risk.

### Section 1.8: Lawful Stop and Closure

Supported by:

- Anthropic, *Measuring AI agent autonomy in practice*
- Anthropic, *Effective harnesses for long-running agents*
- production failure-mode taxonomies

Use:

- This is another strong empirical section.
- Use Anthropic's own engineering/research material to ground the need for agent-initiated stop, clarification, and non-premature closure.

## Integration Guidance

The package README recommends citing only 8-10 references in the final published chapter, not every source in the evidence package.

Good default selection:

- Anthropic, *Building effective agents*
- Anthropic, *Effective context engineering for AI agents*
- Anthropic, *How we built our multi-agent research system*
- Liu et al., *Lost in the Middle*
- Chroma, *Context Rot*
- METR, *Measuring AI Ability to Complete Long Tasks*
- OWASP LLM06
- MCPTox / MCP tool-poisoning evidence
- Anthropic, *Measuring AI agent autonomy in practice*
- Anthropic, *Effective harnesses for long-running agents*

The final v3 article currently cites 19 references. That is acceptable for the PDF edition, but Substack may benefit from a lighter visible reference list with a link back to this evidence index.

