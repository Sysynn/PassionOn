let visibleCountNew = 4
  let visibleCountHot = 4
  const newClothesDiv = document.querySelectorAll('.newClothes')
  const newClothesBtn = document.getElementById('newClothesBtn')
  const hotClothesBtn = document.getElementById('hotClothesBtn')

  newClothesBtn.addEventListener('click', (event) => {
      if (visibleCountNew < 12) {
          for (let idx = 0; idx < 4; idx++) {
              const newClothesItem = document.getElementById(`newClothes${idx + 1 + visibleCountNew}`)
              // console.log(newClothesItem)
              newClothesItem.hidden = false
          }
          visibleCountNew += 4

          // console.log(event.target)
          if (visibleCountNew === 12) {
              event.target.remove()
              // event.target.hidden = true
          }
      }
  })
  hotClothesBtn.addEventListener('click', (event) => {
      if (visibleCountHot < 16) {
          for (let idx = 0; idx < 4; idx++) {
              const hotClothesItem = document.getElementById(`hotClothes${idx + 1 + visibleCountHot}`)
              // console.log(hotClothesItem)
              hotClothesItem.hidden = false
          }
          visibleCountHot += 4

          // console.log(event.target)
          if (visibleCountHot === 16) {
              event.target.remove()
              // event.target.hidden = true
          }
      }
  })