import React, { useState, useEffect } from 'react';

const PrintNotes = () => {
  const [longitude, setLongitude] = useState('');
  const [latitude, setLatitude] = useState('');
  const [civicAddress, setCivicAddress] = useState('');

  useEffect(() => {
    const interval = setInterval(() => {
      fetch('http://127.0.0.1:5000/location')
        .then(response => response.json())
        .then(data => {
          if (data.location) {
            if (data.location.longitude) {
              setLongitude(data.location.longitude);
            } else {
              setLongitude('');
            }
            if (data.location.latitude) {
              setLatitude(data.location.latitude);
            } else {
              setLatitude('');
            }
            if (data.location.civic_address) {
              setCivicAddress(data.location.civic_address);
            } else {
              setCivicAddress('');
            }
          }
        })
        .catch(error => {
          console.error('Error fetching location data:', error);
          setLongitude('');
          setLatitude('');
          setCivicAddress('');
        });
    }, 2000); // Fetch cada 2 segundos

    return () => clearInterval(interval); 
  }, []);

  return (
    <div>
      <h1>Print Notes...</h1>
      <p>Longitude: X</p>
      <p>Latitude: Y</p>
      <p>Civic Address: Street</p>
      <p>Other information...</p>
    </div>
  );
};

export default PrintNotes;
