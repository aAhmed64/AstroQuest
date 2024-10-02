<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>3D VR Solar System</title>
    <link rel="icon" href="img/icon.png">
    <meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
    <link rel="stylesheet" href="css/modalStyle.css">
    <script src="js/libaries/jquery-3.3.1.min.js"></script>
    <script src="js/libaries/bootstrap.bundle.js"></script>
    <script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script>
    <script src="https://rawgit.com/fernandojsg/aframe-teleport-controls/master/dist/aframe-teleport-controls.min.js"></script>

    <script>
        $(document).ready(function () {
            $("#myModal").modal('show');
        });

        document.addEventListener('DOMContentLoaded', function () {
            const entities = document.querySelectorAll('[data-entity-id]');
            const camera = document.querySelector('a-camera');

            entities.forEach(entity => {
                entity.addEventListener('click', function () {
                    moveToEntity(entity);
                });
            });
        });

        function moveToEntity(entity) {
            const camera = document.querySelector('a-camera');
            const targetPosition = entity.getAttribute('data-position');
            if (targetPosition) {
                const [x, y, z] = targetPosition.split(';').map(prop => parseFloat(prop.split(':')[1].trim()));
                // Move camera smoothly to the target
                camera.setAttribute('position', { x: x, y: y, z: z - 5 });
                
                // Optional: Rotation to face the entity
                const rotation = {
                    x: 0,
                    y: x > 0 ? 180 : 0,
                    z: z > 0 ? -90 : 90
                };
                camera.setAttribute('rotation', rotation);
            } else {
                console.error('Entity position not found:', entity);
            }
        }
    </script>
</head>

<body>
    <div class="entity-list-wrapper">
        <h2>Entities</h2>
        <ul id="entity-list">
            <li data-entity-id="sun" data-position="x: -10; y: 5.25; z: -5">Sun</li>
            <li data-entity-id="mercury" data-position="x: -18; y: 1.25; z: -5">Mercury</li>
            <li data-entity-id="venus" data-position="x: -16; y: 1.25; z: -5">Venus</li>
            <li data-entity-id="earth" data-position="x: -14; y: 1.25; z: -5">Earth</li>
            <li data-entity-id="mars" data-position="x: -12; y: 1.25; z: -5">Mars</li>
            <li data-entity-id="jupiter" data-position="x: -10; y: 1.25; z: -5">Jupiter</li>
            <li data-entity-id="saturn" data-position="x: -8; y: 1.25; z: -5">Saturn</li>
            <li data-entity-id="uranus" data-position="x: -6; y: 1.25; z: -5">Uranus</li>
            <li data-entity-id="neptune" data-position="x: -4; y: 1.25; z: -5">Neptune</li>
            <li data-entity-id="2005EU95" data-position="x: -2; y: 1.25; z: -5">2005 EU95</li>
        </ul>
    </div>

    <a-scene>
        <a-camera wasd-controls="acceleration: 300" look-controls position="0 5 0" rotation="-90 0 0"></a-camera>
        <a-assets>
            <img id="sunText" src="img/sun.jpg">
            <img id="mercuryText" src="img/mercury.jpg">
            <img id="venusText" src="img/venus_atmosphere.jpg">
            <img id="earthText" src="img/earth.jpg">
            <img id="marsText" src="img/mars.jpg">
            <img id="jupiterText" src="img/jupiter.jpg">
            <img id="saturnText" src="img/saturn.jpg">
            <img id="uranusText" src="img/uranus.jpg">
            <img id="neptuneText" src="img/neptune.jpg">
            <img id="skyText" src="img/stars.jpg">
        </a-assets>

        <a-sky src="#skyText"></a-sky>
        <a-light type="ambient" color="#222"></a-light>
        <a-light type="spot" angle="180" color="#fff0da" intensity="1.5" position="-20 1.25 -5"></a-light>

        <a-entity id="sun" geometry="primitive: sphere; radius:6;" position="-20 1.25 -5" material="shader: flat; src: #sunText" animation="property: rotation; to: 0 -360 0; easing: linear; loop: true; dur: 200000"></a-entity>

        <!-- Add other planets in similar format -->

    </a-scene>
</body>

</html>