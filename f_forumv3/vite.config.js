import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react";
import tailwind from "@tailwindcss/vite";
import handler from "./api/studio.js";
export default defineConfig(({ mode }) => {
  Object.assign(process.env, loadEnv(mode, process.cwd(), ""));
  return {
    plugins: [
      react(),
      tailwind(),
      {
        name: "studio-api",
        configureServer(server) {
          server.middlewares.use((req, res, next) => {
            if (req.url?.split("?")[0] === "/api/studio")
              void handler(req, res);
            else next();
          });
        },
      },
    ],
    server: { host: "0.0.0.0", allowedHosts: true },
    build: { target: "es2022" },
  };
});
