const fs = require("fs")

// Just used to check all activities in our system
// TODO: Remove when the system is ready

let allAct = []
const infos = JSON.parse(fs.readFileSync("destinyG.json", "utf-8"))
infos.forEach(({ activities }) => {
  activities.forEach(act => {
    const alreadyAdded = allAct.includes(act)
    if (alreadyAdded) return
    allAct.push(act)
  })
})

console.log(allAct);


