console.log("JavaScript is connected!");
const Gojo = document.getElementById("gojo-button");
const Eren = document.getElementById("eren-button");
const Naruto = document.getElementById("naruto-button");
const Luffy = document.getElementById("luffy-button"); 
let fighters = ["Gojo", "Naruto" , "Luffy" , "Eren"]; 
let fighter = " ";
let narutoHealth = 150;
let luffyHealth = 130;
let gojoHealth = 160;
let erenHealth = 155;
function updateHealth() {
if (fighter === "gojo") {document.getElementById("fighter-health").textContent = "Gojo's Health :" + gojoHealth}
else if (fighter === "eren") {document.getElementById("fighter-health").textContent = "eren's health is:" + erenHealth}
else if (fighter === "naruto") {document.getElementById("fighter-health").textContent = "naruto's health :" + narutoHealth}                              
else if (fighter === "luffy") {document.getElementById("fighter-health").textContent = "luffy's health is:" + luffyHealth}};
Gojo.addEventListener("click", () => {fighter = "gojo";document.getElementById("fighter").textContent = "Gojo is selected: HP: 160 | Attack: 35"; updateHealth();});
Eren.addEventListener("click", () => {fighter = "eren";document.getElementById("fighter").textContent ="Eren is selected: HP: " + erenHealth + " | Attack: 30"; updateHealth();});
Naruto.addEventListener("click", () => {fighter = "naruto";document.getElementById("fighter").textContent = "Naruto is selected: HP: 150 | Attack: 30"; updateHealth();});
Luffy.addEventListener("click", () => {fighter = "luffy";document.getElementById("fighter").textContent = "Luffy is selected: HP: 130 | Attack: 20"; updateHealth();});
const enemy = fighters[Math.floor(Math.random()*fighters.length)];
function updateEnemyhealth () {
if (enemy === "Gojo") {document.getElementById("enemy-health").textContent = "Gojo's Health :" + gojoHealth}
else if (enemy === "Eren") {document.getElementById("enemy-health").textContent = "eren's health is:" + erenHealth}
else if (enemy === "Naruto") {document.getElementById("enemy-health").textContent = "naruto's health :" + narutoHealth}                              
else if (enemy === "Luffy") {document.getElementById("enemy-health").textContent = "luffy's health is:" + luffyHealth};};
document.getElementById("enemy").textContent = `${enemy} is the enemy`; updateEnemyhealth ();
function updateShowdownscreen () {
if (fighter === "gojo") {document.getElementById("fighter-ch").textContent = "GOJO VS"}
else if (fighter === "eren") {document.getElementById("fighter-ch").textContent = "EREN VS"}
else if (fighter === "naruto") {document.getElementById("fighter-ch").textContent = "NARUTO VS"}                              
else if (fighter === "luffy") {document.getElementById("fighter-ch").textContent = "LUFFY VS"};}
if (enemy === "Gojo") {document.getElementById("enemy-ch").textContent = "GOJO"}
else if (enemy === "Eren") {document.getElementById("enemy-ch").textContent = "EREN"}
else if (enemy === "Naruto") {document.getElementById("enemy-ch").textContent = "NARUTO"}                              
else if (enemy === "Luffy") {document.getElementById("enemy-ch").textContent = "LUFFY"};
const goingtostart = (document.getElementById("goingtostart"));
goingtostart.addEventListener("click", () => {document.getElementById("starting-screen").style.display="none"});
goingtostart.addEventListener("click",() => {document.getElementById("showdown-screen").style.display="block"});
const startbattle = (document.getElementById("start-battle"));
startbattle.addEventListener("click", () => {document.getElementById("showdown-screen").style.display="none"});
startbattle.addEventListener("click", () => {document.getElementById("battlebegins-screen").style.display="block"});
const load = (document.getElementById("load"));
load.addEventListener("click", () => {document.getElementById("battlebegins-screen").style.display="none"});
load.addEventListener("click", () => {document.getElementById("battle-screen").style.display="block"});
const neartoend = (document.getElementById("neartoend"));
neartoend.addEventListener("click", () => {document.getElementById("battle-screen").style.display="none"});
neartoend.addEventListener("click", () => {document.getElementById("ending-screen").style.display="block"});
const attack = (document.getElementById("attack"));
const defence = (document.getElementById("defence"));
