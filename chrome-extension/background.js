chrome.browserAction.onClicked.addListener(function () {
  fetch('https://youtube-to-snipd.pandibay.com?id=x7RRJhhAEfk', { method: 'GET' })
    .then((response) => response.text())
    .then((data) => {
      alert(data);
    });
});
