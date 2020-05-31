import React from "react";
import { Switch, Route } from "react-router-dom";

import Home from "./pages/Home";
import Map from "./pages/Map";
import ProcessedImage from "./pages/ProcessedImage";

export default function App() {
  return (
    <Switch>
      <Route path="/" exact component={Home} />
      <Route path="/map" exact component={Map} />
      <Route path="/result" exact component={ProcessedImage} />
    </Switch>
  );
}
