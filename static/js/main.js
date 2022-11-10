const copyUrl = () => {
    const copyText = document.getElementById("short_link");

    copyText.select();
    copyText.setSelectionRange(0, 99999);

    document.execCommand("copy");

    alert("Copied the text: " + copyText.value);
}

const copyToClipboard = (e) => {
    let tooltip = e.target.parentNode.querySelector(".tooltip");
    let text = e.target.innerText;

    navigator.clipboard.writeText(text)
        .then(() => tooltip.innerText = "Copied")
        .catch(err => alert(err));
}

const onOut = (e) => {
    let tooltip = e.target.parentNode.querySelector(".tooltip");
    tooltip.innerText = "Copy to clipboard";
}

const copyableButtons = document.querySelectorAll(".copyable");
copyableButtons.forEach(button => {
    button.addEventListener("click", copyToClipboard);
    button.addEventListener("mouseleave", onOut);
});


const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const deleteSmrl = (e) => {
    const target = e.target;
    const row = target.parentNode.parentNode;
    const id = target.dataset.id;
    const url = target.dataset.url;

    $('.ui.basic.modal')
        .modal({
            onApprove: function () {
                $.ajax({
                    type: 'POST',
                    url: url,
                    data: {
                        'csrfmiddlewaretoken': getCookie('csrftoken'),
                        'smrl_id': id
                    },
                    success: function (response) {
                        console.log(response);
                        row.parentNode.removeChild(row);
                        // location.reload();
                    },
                    error: function (error) {
                        console.log(error);
                    }
                })
            }
        })
        .modal('show');
}


$('.message .close').on('click', function () {
    $(this)
        .closest('.message')
        .transition('fade')
        ;
});
