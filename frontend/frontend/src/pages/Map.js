import React, { useState } from "react";
import { Link } from "react-router-dom";
import GoogleMap from "google-map-react";
import GooglePlacesAutocomplete, {
  geocodeByPlaceId,
  getLatLng,
} from "react-google-places-autocomplete";

import html2canvas from "html2canvas";

import { FaArrowLeft } from "react-icons/fa";

import api from "../services/api";
import history from "../services/history";

import Marker from "../marker";

export default function App() {
  const map = React.useRef();
  const [image, setImage] = React.useState("");
  const [showMap, setShowMap] = React.useState(false);
  const [zoom, setZoom] = React.useState(18);
  const [draggable, setDraggable] = useState(true);
  const [latitude, setLatitude] = useState(Number(-19.9167));
  const [longitude, setLongitude] = useState(Number(-43.9345));
  const [markerLat, setMarkerLat] = useState(latitude);
  const [markerLng, setMarkerLng] = useState(longitude);

  const center = {
    lat: latitude,
    lng: longitude,
  };

  const onMouseDown = (childKey, childProps, mouse) => {
    setDraggable(false);
  };

  const onMouseMove = (childKey, childProps, mouse) => {
    setMarkerLat(mouse.lat);
    setMarkerLng(mouse.lng);
  };

  const onMouseUp = (childKey, childProps, mouse) => {
    setMarkerLat(mouse.lat);
    setMarkerLng(mouse.lng);
    setLatitude(mouse.lat);
    setLongitude(mouse.lng);
  };

  const SendImage = async () => {
    html2canvas(document.querySelector("#mapa"), {
      useCORS: true,
      allowTaint: true,
      async: false,
    }).then((canvas) => {
      const base64 = canvas.toDataURL("image/png");
      console.log(123, base64);
      api
        .post("/vision", {
          image_base64: base64,
        })
        .then(
          (response) => {
            console.log(543, response);
            history.push(`/result/`, {
              image: response.data,
            });
          },
          (error) => {
            console.log(error);
          }
        );
    });
  };

  return (
    <div className="App">
      <Link
        to="/"
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
      {image.length > 0 && (
        <button onClick={() => setImage("")}>Erase image</button>
      )}
      <img id="googlemapbinary" src={image} />
      <strong>
        Search your place:
        <GooglePlacesAutocomplete
          apiKey="COLOQUE SUA APIKEY AQUI"
          placeholder="Type your address first..."
          onSelect={(e) => {
            geocodeByPlaceId(e.place_id)
              .then((results) => getLatLng(results[0]))
              .then(({ lat, lng }) => {
                setMarkerLat(lat);
                setMarkerLng(lng);
                setLatitude(lat);
                setLongitude(lng);
                console.log("Successfully got latitude and longitude", {
                  lat,
                  lng,
                });
              });
            setShowMap(true);
          }}
        />
      </strong>
      <section
        id="mapa"
        style={{ position: "relative", width: "800px", height: "600px" }}
      >
        {showMap && (
          <GoogleMap
            ref={map}
            defaultZoom={zoom}
            onZoomChanged={(value) => setZoom(value)}
            center={center}
            draggable={draggable}
            onChildMouseDown={onMouseDown}
            onChildMouseMove={onMouseMove}
            onChildMouseUp={onMouseUp}
            options={(map) => ({ mapTypeId: map.MapTypeId.SATELLITE })}
          >
            <Marker lat={markerLat} lng={markerLng} />
          </GoogleMap>
        )}
      </section>
      {showMap && <button onClick={SendImage}>Process image</button>}
    </div>
  );
}
