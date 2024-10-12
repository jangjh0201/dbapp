// 모달 열기
function openAddModal() {
    document.getElementById('add-beverage-modal').style.display = 'block';
}

// 모달 닫기
function closeAddModal() {
    document.getElementById('add-beverage-modal').style.display = 'none';
}

// 모달 외부 클릭 시 닫기
function closeOnOutsideClick(event) {
    if (event.target.id === 'add-beverage-modal') {
        closeAddModal();
    }
}

function orderBeverage(beverageId) {
    $.ajax({
        url: '/beverage/order/' + beverageId,
        type: 'PUT',
        success: function (response) {
            if (response.success) {
                location.reload(); // 주문 성공 후 페이지 새로고침
            } else {
                alert('음료 주문에 실패했습니다.');
            }
        },
        error: function (error) {
            alert('음료 주문 중 오류가 발생했습니다.');
        }
    });
}

function refillBeverage(beverageId) {
    $.ajax({
        url: '/beverage/refill/' + beverageId,
        type: 'PUT',
        success: function (response) {
            if (response.success) {
                location.reload(); // 보충 성공 후 페이지 새로고침
            } else {
                alert('음료 보충에 실패했습니다.');
            }
        },
        error: function (error) {
            alert('음료 보충 중 오류가 발생했습니다.');
        }
    });
}

function deleteDispenser(beverageId) {
    $.ajax({
        url: '/beverage/' + beverageId,
        type: 'DELETE',
        success: function (response) {
            location.reload(); // 디스펜서 삭제 후 페이지 새로고침
        },
        error: function (error) {
            alert('디스펜서를 삭제하는 중 오류가 발생했습니다.');
        }
    });
}

function addBeverage() {
    const name = $('#beverage-name').val();
    const quantity = parseInt($('#beverage-quantity').val(), 10);

    if (name && quantity > 0) {
        $.ajax({
            url: '/beverage',
            type: 'POST',
            data: { name: name, quantity: quantity },
            contentType: 'application/x-www-form-urlencoded',
            success: function (response) {
                location.reload(); // 음료 추가 후 페이지 새로고침
            },
            error: function (error) {
                alert('음료를 추가하는 중 오류가 발생했습니다.');
            }
        });
    } else {
        alert('유효한 음료 이름과 수량을 입력하세요.');
    }
}
