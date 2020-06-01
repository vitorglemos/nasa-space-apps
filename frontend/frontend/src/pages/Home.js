import React from "react";
import { Link } from "react-router-dom";

import { FaArrowRight } from "react-icons/fa";

export default function Home() {
  return (
    <div>
      <Link className="Home" to="/map">
        <orange>Track</orange> <red>Covid-19</red>{" "}
        <cta>
          Start the mission <FaArrowRight size={22} />
        </cta>
      </Link>
    </div>
  );
}
