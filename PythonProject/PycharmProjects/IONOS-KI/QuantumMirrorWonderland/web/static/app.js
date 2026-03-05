// app.js - Sacred Geometry + Agent Orbits + Chat

class SacredGeometry {
  constructor() {
    this.canvas = document.getElementById('sacred-geometry-canvas');
    if(!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.resize();
    window.addEventListener('resize', () => this.resize());
    this.time = 0;
    requestAnimationFrame(() => this.animate());
  }

  resize(){
    this.width = this.canvas.width = this.canvas.offsetWidth;
    this.height = this.canvas.height = this.canvas.offsetHeight;
    this.cx = this.width/2; this.cy = this.height/2;
  }

  drawRing(x,y,r,alpha=0.3){
    this.ctx.strokeStyle = `rgba(255,215,0,${alpha})`;
    this.ctx.lineWidth = 1.5; this.ctx.beginPath(); this.ctx.arc(x,y,r,0,Math.PI*2); this.ctx.stroke();
  }

  draw(){
    const mainR=120; const petals=6;
    this.drawRing(this.cx,this.cy,30,0.5);
    for(let i=0;i<petals;i++){const a=(i/petals)*Math.PI*2;const x=this.cx+Math.cos(a)*mainR;const y=this.cy+Math.sin(a)*mainR;this.drawRing(x,y,mainR,0.2)}
    const outer=180; for(let i=0;i<12;i++){const a=(i/12)*Math.PI*2;const x=this.cx+Math.cos(a)*outer;const y=this.cy+Math.sin(a)*outer;this.drawRing(x,y,40,0.12)}
    const pulse=60+Math.sin(this.time*0.005)*10; this.ctx.strokeStyle=`rgba(0,255,127,${0.4+Math.sin(this.time*0.003)*0.2})`; this.ctx.lineWidth=2; this.ctx.beginPath(); this.ctx.arc(this.cx,this.cy,pulse,0,Math.PI*2); this.ctx.stroke();
  }

  animate(){
    if(!this.ctx) return; this.ctx.clearRect(0,0,this.width,this.height); this.draw(); this.time++; requestAnimationFrame(()=>this.animate());
  }
}

class QuantumAgentCentral{
  constructor(){
    this.agents=[
      {id:'singulos',name:'Singulos',img:'/static/assets/agent-singulos.svg'},
      {id:'ionos7',name:'IONOS-7',img:'/static/assets/agent-ionos7.svg'},
      {id:'ultra',name:'Ultra',img:'/static/assets/agent-ultra.svg'},
      {id:'nexus',name:'Nexus',img:'/static/assets/agent-nexus.svg'},
      {id:'quantum',name:'Quantum',img:'/static/assets/agent-quantum.svg'},
      {id:'spark',name:'Spark',img:'/static/assets/agent-spark.svg'},
      {id:'nova',name:'Nova',img:'/static/assets/agent-nova.svg'},
      {id:'zenith',name:'Zenith',img:'/static/assets/agent-zenith.svg'},
      {id:'aether',name:'Aether',img:'/static/assets/agent-aether.svg'},
      {id:'infinity',name:'Infinity',img:'/static/assets/agent-infinity.svg'}
    ];
    this.active=1; this.init();
  }
  init(){
    this.renderOrbits();
    document.getElementById('chat-send').addEventListener('click',()=>this.send());
    document.getElementById('chat-input').addEventListener('keypress',e=>{if(e.key==='Enter')this.send()});
    document.getElementById('close-chat').addEventListener('click',()=>{document.getElementById('chat-container').style.display='none'})
  }
  renderOrbits(){
    const container=document.getElementById('agents-orbit'); if(!container) return; container.innerHTML='';
    const radius=350; const cx=400,cy=400; // container center (CSS)
    this.agents.forEach((a,i)=>{
      const el=document.createElement('div'); el.className='agent-orbit'; el.dataset.agent=a.id; el.style.animationDelay=`-${i*3}s`;
      const inner=document.createElement('div'); inner.className='agent-avatar';
      // Use image
      const img=document.createElement('img'); img.src=a.img; img.alt=a.name; img.style.width='80%'; img.style.height='80%'; img.style.borderRadius='50%';
      const name=document.createElement('div'); name.className='agent-name'; name.textContent=a.name;
      inner.appendChild(img); inner.appendChild(name); el.appendChild(inner);
      el.addEventListener('click',()=>this.activate(i)); el.addEventListener('mouseenter',()=>inner.style.transform='scale(1.05)'); el.addEventListener('mouseleave',()=>inner.style.transform='scale(1)');
      container.appendChild(el);
    });
    // set initial active
    this.activate(this.active);
  }
  activate(i){
    this.active=i; document.querySelectorAll('.agent-orbit').forEach(el=>el.classList.remove('active'));
    const el=document.querySelector(`.agent-orbit[data-agent="${this.agents[i].id}"]`); if(el)el.classList.add('active');
    document.getElementById('active-agent-icon').textContent='⚡';
    document.getElementById('active-agent-name').textContent=this.agents[i].name;
    document.getElementById('chat-agent-name').textContent=this.agents[i].name;
    this.postSystemMessage(`Agent ${this.agents[i].name} ist nun aktiv!`);
    document.getElementById('chat-container').style.display='flex';
  }
  postSystemMessage(msg){const m=document.createElement('div');m.className='chat-message agent-message';m.innerHTML=`<strong>${this.agents[this.active].name}:</strong> ${msg}`;document.getElementById('chat-messages').appendChild(m);document.getElementById('chat-messages').scrollTop=document.getElementById('chat-messages').scrollHeight}
  send(){const input=document.getElementById('chat-input');const v=input.value.trim(); if(!v) return; const um=document.createElement('div');um.className='chat-message user-message';um.innerHTML=`<strong>Du:</strong> ${v}`;document.getElementById('chat-messages').appendChild(um);input.value='';setTimeout(()=>{this.postAgentResponse(v)},500)}
  postAgentResponse(userInput){const responses={ionos7:[`IONOS-7 analysiert: ${userInput}`,`Blitzschnelle Verarbeitung... erledigt!`],singulos:[`Die Singularität beobachtet: ${userInput}`,'Im Kern der Unendlichkeit erkenne ich...'],ultra:[`Ultra Mode activated: ${userInput}`,'Maximale Leistung erreicht!'],nexus:['Nexus verbindet Datenströme...','Neuronale Netzwerke resonieren...'],quantum:['Quantensprung eingeleitet...','Superposition erkannt...'],spark:['Kreative Funken sprühen!','Innovation in vollem Gange'],nova:['Nova expandiert...','Strahlende Antwort!'],zenith:['Zenith erreicht Höhepunkt','Gipfelleistung garantiert'],aether:['Äther flüstert Weisheit...','Kosmische Wahrheiten...'],infinity:['Unendliche Möglichkeiten...','Ohne Grenzen...']}; const agentId=this.agents[this.active].id; const opts=responses[agentId]||['Verarbeitung läuft...']; const res=opts[Math.floor(Math.random()*opts.length)]; const m=document.createElement('div');m.className='chat-message agent-message';m.innerHTML=`<strong>${this.agents[this.active].name}:</strong> ${res}`;document.getElementById('chat-messages').appendChild(m);document.getElementById('chat-messages').scrollTop=document.getElementById('chat-messages').scrollHeight}
}

// Init on DOMContentLoaded
window.addEventListener('DOMContentLoaded',()=>{new SacredGeometry();new QuantumAgentCentral();console.log('Initialized')});
