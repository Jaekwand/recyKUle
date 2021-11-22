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
    let newContent = ``;
    for (const item of responseBody['payload']) {
        newContent += `
            <div class="container-fluid d-flex justify-content-center">
                <div class="card" style="width:70%;">
                  <div class="card-body">
                    <h5 class="card-title">${item.artist_name}</h5>
                    <h6 class="card-subtitle mb-2 text-muted">
                        ${item.expensive_artwork_title}
                    </h6>
                    <p class="card-text">
                       ${item.expensive_artwork_price}
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
