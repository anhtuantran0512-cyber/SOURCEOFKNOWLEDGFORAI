import React from "react";
import "./src/index.css";
import "./src/styles/forumDesignSystem.css";
import "./src/styles/responsiveExperience.css";
import "./src/styles/fabulousTheme.css";
import "./src/styles/warmEditorialBrutalism.css";
import LandingPage from "./src/components/landing/LandingPage.tsx";
export default function Entry() {
  const open = () => location.assign("/home");
  const sign = () => location.assign("/home?auth=1");
  return (
    <LandingPage
      currentUser={null}
      onOpenAuth={open}
      onOpenLogin={sign}
      onEnterApp={open}
      onNavigate={(view) =>
        location.assign(
          {
            clubs: "/community",
            qa: "/community",
            threads: "/community",
            "exam-vault": "/explore",
            chat: "/workspace",
          }[view] || "/home",
        )
      }
    />
  );
}
