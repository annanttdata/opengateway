import React, { useState, useEffect, useRef } from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

const containerStyle = {
  width: '100vw',
  height: '100vh'
};

const center = {
  lat: 41.3851,
  lng: 2.1734
};

const Map = () => {
  const [markers, setMarkers] = useState([]);
  const mapRef = useRef(null); // Ref to GoogleMap
  const lastCircleRef = useRef(null); // Ref to the last circle

  useEffect(() => {
    const interval = setInterval(() => {
      fetch('http://127.0.0.1:5000/localization')
        .then(response => response.json())
        .then(data => {
          const newMarkers = [];
          if (data.gps) {
            newMarkers.push({ name: 'gps', ...data.gps });
          }
          if (data.network_as_code) {
            newMarkers.push({ name: 'network_as_code', ...data.network_as_code });
          }
          setMarkers(newMarkers);
        })
        .catch(error => {
          console.error('Error fetching localization:', error);
          setMarkers([]);
        });
    }, 2000); // Fetch each 2 seconds

    return () => clearInterval(interval); 
  }, []);

  useEffect(() => {
    if (mapRef.current && markers.length === 2) {
      drawCircle();
    }
  }, [markers]); // This useEffect depends on the `markers`

  const drawCircle = () => {
    if (lastCircleRef.current) {
      lastCircleRef.current.setMap(null); 
    }

    const circle = new window.google.maps.Circle({
      map: mapRef.current,
      center: {
        lat: (markers[0].latitude + markers[1].latitude) / 2,
        lng: (markers[0].longitude + markers[1].longitude) / 2,
      },
      radius: getDistance(markers[0], markers[1]) / 2,
      strokeColor: "#FF0000",
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillColor: "#FF0000",
      fillOpacity: 0.35,
    });

    lastCircleRef.current = circle;
  };

  return (
    <LoadScript googleMapsApiKey="YOUR_API_KEY">
      <GoogleMap
        mapContainerStyle={containerStyle}
        center={center}
        zoom={10}
        onLoad={mapInstance => mapRef.current = mapInstance}
      >
        {markers.map((marker, index) => (
          <Marker
            key={index}
            position={{ lat: marker.latitude, lng: marker.longitude }}
            label={marker.name}
          />
        ))}
      </GoogleMap>
    </LoadScript>
  );
};

function getDistance(marker1, marker2) {
  const lat1 = marker1.latitude;
  const lon1 = marker1.longitude;
  const lat2 = marker2.latitude;
  const lon2 = marker2.longitude;

  const R = 6371; // World radio
  const dLat = deg2rad(lat2 - lat1);
  const dLon = deg2rad(lon2 - lon1);
  const a =
    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) *
    Math.sin(dLon / 2) * Math.sin(dLon / 2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  const distance = R * c; +
  return distance * 1000; 
}

function deg2rad(deg) {
  return deg * (Math.PI / 180);
}

export default Map;