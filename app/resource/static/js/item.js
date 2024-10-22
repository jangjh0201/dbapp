// 모달 열기
function openAddModal() {
    document.getElementById('add-item-modal').style.display = 'block';
}

// 모달 닫기
function closeAddModal() {
    document.getElementById('add-item-modal').style.display = 'none';
}

// 모달 외부 클릭 시 닫기
function closeOnOutsideClick(event) {
    if (event.target.id === 'add-item-modal') {
        closeAddModal();
    }
}

// 아이템 추가
function addItem() {
    const name = $('#item-name').val(); // 물품 이름만 받음

    if (name.trim()) {
        $.ajax({
            url: '/item',
            type: 'POST',
            data: { name: name },
            success: function (response) {
                alert('등록되었습니다.');
                location.reload(); // 성공 시 페이지 새로고침
            },
            error: function (error) {
                alert('물품 등록 중 오류가 발생했습니다.');
            }
        });
    } else {
        alert('유효한 물품 이름을 입력하세요.');
    }
}

// 아이템 삭제
function deleteItem(itemId) {
    $.ajax({
        url: `/item/${itemId}`,
        type: 'DELETE',
        success: function (response) {
            if (response.success) {
                alert('삭제되었습니다.');
                location.reload(); // 삭제 후 새로고침
            } else {
                alert('물품 삭제에 실패했습니다.');
            }
        },
        error: function (error) {
            alert('물품을 삭제하는 중 오류가 발생했습니다.');
        }
    });
}

// 아이콘 상태 변경 (cabinet_store <-> cabinet_use)
function toggleIcon(icon, itemId) {
    const currentSrc = icon.getAttribute('src');
    const isStoring = currentSrc.includes('cabinet_store');
    const newSrc = isStoring
        ? '/static/images/cabinet_use.png'
        : '/static/images/cabinet_store.png';

    // 아이콘 상태 변경
    icon.setAttribute('src', newSrc);

    // 상태를 서버에 전달
    const actionUrl = isStoring ? `/item/${itemId}/use` : `/item/${itemId}/keep`;

    $.ajax({
        url: actionUrl,  // '/item/1/use' 또는 '/item/1/keep' 로 요청됨
        type: 'PUT',
        success: function (response) {
            if (response.success) {
                console.log('상태 변경 성공');
            } else {
                alert('상태 변경에 실패했습니다.');
            }
        },
        error: function (error) {
            console.error('Error:', error);
            alert('상태 변경 중 오류가 발생했습니다.');
        }
    });
}

// 모달 외부 클릭 이벤트 등록
document.addEventListener('click', closeOnOutsideClick);
