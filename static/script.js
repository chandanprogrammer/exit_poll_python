function clearResult() {
    // Hide result text
    const box = document.querySelector(".result-box");
    const clearBtn = document.querySelector(".clear-btn");

    if (box) box.style.display = "none";
    if (clearBtn) clearBtn.style.display = "none";

    // Scroll card to top smoothly
    const card = document.querySelector(".glass-card");
    if (card) {
        card.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    }
}
