function bgColor() {
    const anchor = document.querySelector(".entry-tag a");
    let text = anchor.text;

    let tagCourse = text.includes("Turkish")
    let tagCategory = text.includes("category")

    let availableColors = [
        "#84B4A8",
        "#FFFFFD",
        "#5D3C2D",
        "#FBF8F3",
        "#000000",
        "#EAE2D7",
        "#000000",
        "#58504C",
        "#CAE9E1",
        "#66ADE9",
        "#FA1045"
      ];

      tagCourse.map(function (s, i) {
        s[i].style.color = availableColors[i];

      });


}