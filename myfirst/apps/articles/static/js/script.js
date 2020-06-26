const comments = document.querySelectorAll('.comment')
const replyBtns = document.querySelectorAll('.reply-btn')
const replyBtn = document.querySelector('.reply-btn')
const closeFormBtns = document.querySelectorAll('.close-btn')

let makeElement = function(tagname, cls, value) {
	elem = document.createElement(tagname)
	elem.classList.add(cls)
	elem.textContent = value

	return elem
}

 let toggleReplyForm = () => {
 	replyBtns.forEach(elem => {
		elem.addEventListener('click', e => {
			e.preventDefault()
			let comment = elem.parentNode
			let authorName = comment.querySelector('strong')
			let replyForm = comment.querySelector('.reply-form')
			if (replyForm.hasAttribute('hidden')) {
				replyForm.removeAttribute('hidden')
				let replyText = replyForm.querySelector('textarea')
				replyText.innerHTML = authorName.textContent + ','
				elem.style.display = 'none'
			}
		})
	})

	// closeFormBtns.forEach(btn => {
	// 	btn.addEventListener('click', e => {
	// 		e.preventDefault()
	// 		let replyForm = btn.parentNode
	// 		let comment = replyForm.parentNode
 // 			let replyBtn = makeElement('a', 'reply-btn', 'Reply') 
	// 		if (!replyForm.hasAttribute('hidden')) {
 // 				replyForm.setAttribute('hidden', 'hidden')
 // 				replyBtn.style.display = 'inline'
 // 				comment.innerHTML = `<a href='#' class='reply-btn'>reply</a>`
 // 			}
	// 	})
	// })
 }


toggleReplyForm()
