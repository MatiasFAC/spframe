const list_dom = document.getElementById("list");

url = "http://127.0.0.1:8000/list_img"
let text = "";

function get_list_img(value) {
    text += "<tr><th scope='row'>"+ value["sort"]+"</th><td>"+ value["name"]+ "</td><td>"+ value["time"]+ "</td><td><img src='"+ value["url"]+"' style='max-height: 286px; max-width: 180px;' class='img-thumbnail rounded center'></td></tr>";
}
let fetchRes = fetch(url);
    fetchRes.then(res =>
        res.json()).then(d => {
            console.log(d["list_img"][0])
            d["list_img"].forEach(get_list_img);
            list_dom.innerHTML = text
        })
