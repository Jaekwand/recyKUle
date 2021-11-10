async function onSearch() {
    const searchKeyword = document.querySelector('#searchField').value;
    // fetch
    let response = await fetch("/test", {
        method: "POST",
        headers: {
            "Content-Type": "application/json;charset=utf-8",
            "X-CSRFToken": getCsrfToken(),
        },
        body: JSON.stringify({"keyword": searchKeyword})
    });
    let responseBody = await response.json();

    // let responseBody = {
    //     payload: [
    //         {
    //             "title": "최고의 작품",
    //             "artist": "정승연",
    //             "art_image": "background_image_QlmWsZU.jpeg"
    //         }
    //     ]
    // }
    let newContent = ``;
    for (const item of responseBody['payload']) {
        newContent += `
            <div class="container-fluid d-flex justify-content-center">
                <div class="card" style="width:70%;">
                  <div class="card-body">
                    <h5 class="card-title">No Title</h5>
                    <h6 class="card-subtitle mb-2 text-muted">${item.artist}</h6>
                    <p class="card-text">
<!--                    Some quick example text to build on the card title and make up the bulk of the card's content.-->
                       ${item["recent_selling"]}
                    </p>
                    <a href="#" class="card-link">Card link</a>
                    <a href="#" class="card-link">Another link</a>
                      <div>
                          
                      </div>
                  </div>
                </div>
            </div>`
    }

    document.querySelector('#art-area').innerHTML = newContent;
}

function getCsrfToken(){
    return document.cookie.split(';')
        .find((item) => item.includes('csrftoken'))
        .split('=')[1];
}
