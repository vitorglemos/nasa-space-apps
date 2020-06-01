import React from "react";
import { Link } from "react-router-dom";

import { FaArrowLeft } from "react-icons/fa";

export default function ProcessedImage(props) {
  return (
    <div className="App">
      <Link
        to="/map"
        style={{
          position: "absolute",
          left: 0,
          color: "#fff",
          fontSize: 22,
          margin: 15,
          textDecoration: "none",
        }}
      >
        <FaArrowLeft size={22} /> Go back
      </Link>

      <img
        style={{ marginTop: "50px" }}
        src={
          props?.location?.state?.image?.length > 0
            ? props.location.state.image
            : ""
        }
      />
    </div>
  );
}
