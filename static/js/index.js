$(document).ready(function(){

	var script = document.createElement('script');

	script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyB0BLe3pVR1PBJBX3S3xeJS30yZzmWQgPs';
	script.async = true;
	document.head.appendChild(script);


	let i = 0

	let quotes = [
		["I am glad you asked. This is the address: ",
		"By the way, here is a little anecdote about the area ! "],
		["Hmm, I think I know this place... Let me think.. I remember the address now ! ",
		"Here is an interesting fact about the area ! "], 
		["Well, I think this might help you: ", "Wait, I've got something for your personal knowledge: "]

	]

	class UserMessage {
		constructor(message) {
			this.message = message;
		}

		createDOMElement() {
			this.chat = document.querySelector("#chat")
			let templateInstance = document.querySelector('#user-template')
			this.clone = templateInstance.content.cloneNode(true);
		}

		display() {
			let pId = "usermessage".concat(i);
			this.clone.querySelector('p').id = pId;
			this.chat.appendChild(this.clone);
			$(`#${pId}`).html(this.message)
		}

	}


	class GrandPyMessage {
		constructor(data) {
			this.data = data;
		}

		createDOMElement() {
			this.chat = document.querySelector("#chat")
			let templateInstance = document.querySelector('#grandpy-template')
			this.clone = templateInstance.content.cloneNode(true);
			this.nodes = this.clone.querySelectorAll('p');
			this.div = this.clone.querySelectorAll('div');
			this.a = this.clone.querySelectorAll('a')
		}

		displayWhenOk() {
			let address = this.nodes[0]
			address.id = "address".concat(i)
			let anecdote = this.nodes[1]
			anecdote.id = "anecdote".concat(i)
			let url = this.a[0]
			url.href = this.data.url
			let map = this.div[3];
			map.id = "map".concat(i)
			this.chat.appendChild(this.clone);

			let quoteNumber = Math.floor(Math.random() * 3)

			$(`#${address.id}`).html(quotes[quoteNumber][0] + this.data.address +".");
			$(`#${anecdote.id}`).html(quotes[quoteNumber][1] + this.data.anecdote);
			$(`#${map.id}`).addClass("map");
			return map.id
		}

		displayWhenNok() {
			let message = this.nodes[0]
			this.nodes[1].remove()
			this.div[3].remove()
			let error_message = "Well, I don't understand your question sweetheart... Can you be more specific?"
			message.id = "message".concat(i)
			this.a[0].remove()
			this.clone.querySelectorAll('br')[0].remove()
			this.chat.appendChild(this.clone);

			$(`#${message.id}`).html(error_message)

		}
	}


	$('form').on('submit', (event) => {

		let user_question = $('#question').val();
		$('#form').trigger("reset");

		question = new UserMessage(user_question)
		question.createDOMElement()
		question.display()

		$.ajax({
			type: 'POST',
			url: '/process/',
			data: JSON.stringify({question: user_question}),
			contentType: 'application/json',
			beforeSend: function() {
				let chat = document.querySelector("#chat")
				let templateInstance = document.querySelector('#loading-template')
				let clone = templateInstance.content.cloneNode(true);
				chat.appendChild(clone);
			},

			success: (data) => {
				$('.loading').remove();
				let message = new GrandPyMessage(data)
				message.createDOMElement()

				if (data.status == 'ok') {
					map_id = message.displayWhenOk()
					let coordonates = {lat: data.latitude, lng: data.longitude}
					let options = {
						zoom: 15,
						center: coordonates
					}
					let map = new google.maps.Map(document.getElementById(map_id), options);
					let marker = new google.maps.Marker({
						position: coordonates, 
						map: map
					})

				} else {
					message.displayWhenNok()
				}

				i = ++i

				
			}
		});

		event.preventDefault();

		});
});