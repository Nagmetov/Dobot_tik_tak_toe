const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
const snap = document.getElementById('snap');

navigator.mediaDevices.getUserMedia({ video: true })
    .then((stream) => {
        video.srcObject = stream;
    })
    .catch((err) => {
        console.error('Ошибка доступа к камере: ', err);
    });

function captureFrame() {
    context.drawImage(video, 0, 0, 640, 480);
    const dataURL = canvas.toDataURL('image/png');
    
    fetch('/upload', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ image: dataURL }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            console.log('Изображение успешно загружено!');
        } else {
            console.log('Ошибка загрузки изображения!');
        }
    })
    .catch((error) => {
        console.error('Ошибка:', error);
    });
}

snap.addEventListener('click', () => {
    captureFrame();
});
