async function onSearch() {
    const searchKeyword = document.querySelector('#search').value;
    // fetch
    let responseBody = {
        payload: [
            {
                "title": "asdf",
                "artist": "aquashdw",
                "art_image": "background_image_QlmWsZU.jpeg"
            }
        ]
    }

    let newContent = ``;
    for (const item of responseBody['payload']) {
        newContent += `
            <div class="container-fluid d-flex justify-content-center">
                <div class="card" style="width:70%;">
                  <div class="card-body">
                    <h5 class="card-title">${item.title}</h5>
                    <h6 class="card-subtitle mb-2 text-muted">${item.artist}</h6>
                    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    <a href="#" class="card-link">Card link</a>
                    <a href="#" class="card-link">Another link</a>
                      <div>
                          ${item.art_image}
                      </div>
                  </div>
                </div>
            </div>`
    }

    document.querySelector('#art-area').innerHTML = newContent;
}