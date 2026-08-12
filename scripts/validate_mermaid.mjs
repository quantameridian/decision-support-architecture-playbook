import { readFile, readdir } from "node:fs/promises";
import path from "node:path";
import { JSDOM } from "jsdom";

const dom = new JSDOM("<!doctype html><html><body></body></html>");
globalThis.window = dom.window;
globalThis.document = dom.window.document;

const { default: mermaid } = await import("mermaid");
mermaid.initialize({ startOnLoad: false, securityLevel: "strict" });

const diagramDirectory = "diagrams";
const files = (await readdir(diagramDirectory))
  .filter((name) => name.endsWith(".mmd"))
  .sort();

if (files.length < 7) {
  throw new Error(`Expected at least 7 Mermaid diagrams, found ${files.length}`);
}

for (const file of files) {
  const source = await readFile(path.join(diagramDirectory, file), "utf8");
  const result = await mermaid.parse(source);
  console.log(`Parsed ${file} as ${result.diagramType}`);
}
