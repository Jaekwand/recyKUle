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
            <div class="container-fluid d-flex justify-content-center mt-4">
                <div class="card" style="width:70%;">
                    <div class="card-body">
                        <div class="row g-0 justify-content-between align-items-center" style="height: 100%">
                            <div class="col-md-3 d-flex justify-content-center">
                              <div style="height: 120px; width: 120px; display: inline-block;">
                                <img src="${item.artist_image_url}" 
                                     class="img-fluid  rounded-circle overflow-hidden"
                                     style="width: 100%; height: 100%; object-fit: cover;">
                              </div>
                            </div>
                            <div class="col-md-7">
                                <h5 class="card-title">${item.artist_name}</h5>
                                <h6 class="card-subtitle mb-2 text-muted">최근 거래일 : ${item.recent_artwork_date}</h6>
                                <h6 class="card-subtitle mb-2 text-muted">작품명 : ${item.recent_artwork_title }</h6>
                                <p class="card-text">작품가 : ${item.recent_artwork_price}</p>
                            </div>
                            <div class="col-md-2 d-flex justify-content-center">
                                <button type="button" class="bt btn-secondary ms-3" onclick="location.href='/artist/{{ content.artist.id }}'">호당 가격 확인하기</button>
                            </div>                            
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
