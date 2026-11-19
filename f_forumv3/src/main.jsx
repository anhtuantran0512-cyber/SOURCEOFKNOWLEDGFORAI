import React from "react";
import { createRoot } from "react-dom/client";
import "@fontsource-variable/inter";
import "@fontsource-variable/geist-mono";
const root = createRoot(document.getElementById("root"));
if (location.pathname === "/")
  import("./legacy/Entry.jsx").then(({ default: Landing }) =>
    root.render(<Landing />),
  );
else
  import("./Studio.jsx").then(({ default: Studio }) => root.render(<Studio />));
