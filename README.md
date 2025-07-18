This project contains:

1. An **MCP-compatible Gradio app** for tool usage via browser and AI agents.
2. An `agent.json` config (for Hugging Face MCP or Playwright-based agents).
3. A sample tool `letter_counter` served via `gradio_mcp_app.py`.

---

## 🚀 Gradio Tool (MCP Enabled)

### File: `gradio_mcp_app.py`

This Gradio app exposes a letter-counting tool to both:

- 🧑 Humans via UI: `http://localhost:7860`
- 🤖 AI agents via MCP: `http://localhost:7860/gradio_api/mcp/sse`

### ✅ Run It

```bash
python gradio_mcp_app.py
