import * as THREE from 'three';
const W=720,H=1280,FPS=25,TOTAL=18.5;
const INK=0x1F1D1A, GREEN=0x2C6D3F, LIGHT=0x7CC090, BG=0xF4F6F6;
const clamp=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const ease=x=>{x=clamp(x);return 1-Math.pow(1-x,3)};
const easeIO=x=>{x=clamp(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2};
const back=x=>{x=clamp(x);const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)};
const seg=(t,a,b)=>clamp((t-a)/(b-a));
const renderer=new THREE.WebGLRenderer({canvas:document.getElementById('gl'),antialias:true,preserveDrawingBuffer:true});
renderer.setPixelRatio(1);renderer.setSize(W,H,false);
renderer.shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFSoftShadowMap;
const scene=new THREE.Scene();scene.background=new THREE.Color(BG);

const cam=new THREE.PerspectiveCamera(34,W/H,0.1,60);
scene.add(new THREE.HemisphereLight(0xffffff,0xbfcfc4,0.9));
const sun=new THREE.DirectionalLight(0xffffff,1.1);sun.position.set(4,9,5);sun.castShadow=true;
sun.shadow.mapSize.set(1024,1024);Object.assign(sun.shadow.camera,{left:-4,right:4,top:4,bottom:-4,near:1,far:25});scene.add(sun);
// diorama
const dio=new THREE.Group();scene.add(dio);
const SR=1.75;
const slab=new THREE.Mesh(new THREE.CylinderGeometry(SR,SR+0.08,0.45,72),[new THREE.MeshStandardMaterial({color:INK,roughness:.8}),new THREE.MeshStandardMaterial({color:0xDDE7E0,roughness:.9}),new THREE.MeshStandardMaterial({color:INK})]);
slab.position.y=-0.225;slab.receiveShadow=true;slab.castShadow=true;dio.add(slab);
const rim=new THREE.Mesh(new THREE.TorusGeometry(SR-0.02,0.035,12,96),new THREE.MeshStandardMaterial({color:GREEN}));rim.rotation.x=Math.PI/2;rim.position.y=0.005;dio.add(rim);
const baseDisc=new THREE.Mesh(new THREE.CircleGeometry(30,48),new THREE.ShadowMaterial({opacity:0.16}));baseDisc.rotation.x=-Math.PI/2;baseDisc.position.y=-0.46;baseDisc.receiveShadow=true;scene.add(baseDisc);
// anillo de bolas blancas
const RR=1.12, K=12, kBlack=3;
const whites=[];
const whiteMat=()=>new THREE.MeshStandardMaterial({color:0xFFFFFF,emissive:0x555555,roughness:.35,metalness:0.0,transparent:true,opacity:1});
const ringAngle=k=>Math.PI/2+ (k-kBlack)*2*Math.PI/K; // kBlack apunta a cámara (+z)
const slotPos=k=>new THREE.Vector3(Math.cos(ringAngle(k))*RR,0,Math.sin(ringAngle(k))*RR);
for(let k=0;k<K;k++){ if(k===kBlack) continue;
  const m=new THREE.Mesh(new THREE.SphereGeometry(0.21,32,24),whiteMat());m.castShadow=true;
  const p=slotPos(k);m.userData={k,p,r:0.21};m.position.set(p.x,0.21,p.z);dio.add(m);whites.push(m);
  const dot=new THREE.Mesh(new THREE.CylinderGeometry(0.26,0.26,0.012,32),new THREE.MeshStandardMaterial({color:0xBFD0C6}));dot.position.set(p.x,0.006,p.z);dio.add(dot);}
const slotBlack=new THREE.Mesh(new THREE.CylinderGeometry(0.26,0.26,0.012,32),new THREE.MeshStandardMaterial({color:0xBFD0C6}));
{const p=slotPos(kBlack);slotBlack.position.set(p.x,0.006,p.z);dio.add(slotBlack);}
const black=new THREE.Mesh(new THREE.SphereGeometry(0.29,40,28),new THREE.MeshStandardMaterial({color:INK,roughness:.25,transparent:false}));black.castShadow=true;dio.add(black);
const nullified=[kBlack-1,kBlack+1,kBlack+2].map(k=>((k%K)+K)%K);
// semillas (Vogel)
const GA=137.50776405*Math.PI/180,NS=190,CS=1.5/Math.sqrt(NS);
const seeds=[];
const col=n=>{const t=n/NS;const a=new THREE.Color(INK),b=new THREE.Color(GREEN),c=new THREE.Color(LIGHT);return t<.62?a.lerp(b,Math.min(1,t*1.6)):b.lerp(c,(t-.62)/.38)};
for(let n=1;n<=NS;n++){const r=CS*Math.sqrt(n),th=n*GA;
  const rad=CS*(0.42+0.12*Math.sqrt(n/NS));
  const m=new THREE.Mesh(new THREE.SphereGeometry(rad,16,12),new THREE.MeshStandardMaterial({color:col(n),roughness:.45}));
  m.castShadow=true;m.userData={x:Math.cos(th)*r,z:Math.sin(th)*r,rad,n};m.scale.setScalar(0.0001);m.position.set(m.userData.x,rad,m.userData.z);dio.add(m);seeds.push(m);}
// carteles dibujados dentro de la escena
function makeSign(lines,w=3.7,h=1.6){
  const cv=document.createElement('canvas');cv.width=1024;cv.height=Math.round(1024*h/w);
  const g=cv.getContext('2d');g.fillStyle='#FFFFFF';g.fillRect(0,0,cv.width,cv.height);
  g.fillStyle='#2C6D3F';g.fillRect(0,0,cv.width,14);
  g.textBaseline='middle';
  const n=lines.length;lines.forEach((l,i)=>{
    g.font=`${l.size||70}px 'DejaVu Serif', serif`;
    const y=cv.height*(i+1)/(n+1)+6;
    let x=44;
    (l.parts||[{t:l.t,c:l.c||'#1F1D1A'}]).forEach(p=>{g.fillStyle=p.c||'#1F1D1A';g.fillText(p.t,x,y);x+=g.measureText(p.t).width;});
  });
  const tex=new THREE.CanvasTexture(cv);tex.colorSpace=THREE.SRGBColorSpace;tex.anisotropy=4;
  const side=new THREE.MeshStandardMaterial({color:INK});
  const front=new THREE.MeshBasicMaterial({map:tex});
  const mesh=new THREE.Mesh(new THREE.BoxGeometry(w,h,0.09),[side,side,side,side,front,side]);
  mesh.position.set(0,2.0+h/2,-1.45);
  const grp=new THREE.Group();grp.add(mesh);
  const post=new THREE.CylinderGeometry(0.04,0.04,2.0,10);
  [-1,1].forEach(sg=>{const p=new THREE.Mesh(post,side);p.position.set(sg*(w/2-0.3),1.0,-1.52);grp.add(p);});
  grp.userData={h};scene.add(grp);return grp;
}
const G='#2C6D3F',K0='#1F1D1A';
const signs={
 A:makeSign([{t:'La bola negra:',size:84},{t:'quién decide',size:78},{parts:[{t:'quién ',c:K0},{t:'cabe',c:G}],size:78}],3.7,2.1),
 B:makeSign([{parts:[{t:'Bola blanca: ',c:K0},{t:'cabe.',c:G}],size:68},{parts:[{t:'Bola negra: ',c:K0},{t:'no cabe.',c:'#8A3B2E'}],size:68}],3.7,1.6),
 C:makeSign([{t:'Nadie explica',size:84},{t:'el voto.',size:84}],3.7,1.7),
 D:makeSign([{t:'Antes de votar:',size:76,c:G},{t:'¿a quién deja fuera',size:68},{t:'esta opción?',size:68}],3.7,2.1)
};
Object.values(signs).forEach(s=>{s.visible=false});
const window_={A:[0.9,4.2],B:[4.2,8.4],C:[8.4,11.0],D:[11.0,14.6]};
// cámara
const look=new THREE.Vector3(0,0.9,0);
function setCamera(t){
  const az=0.55*Math.sin(t*0.42)+0.0;
  const elev=THREE.MathUtils.degToRad(22+ (48)*easeIO(seg(t,14.0,16.4)));
  const R=13.6-2.4*easeIO(seg(t,14.0,16.4));
  cam.position.set(Math.sin(az)*Math.cos(elev)*R,Math.sin(elev)*R,Math.cos(az)*Math.cos(elev)*R);
  const ly=1.75-1.6*easeIO(seg(t,14.0,16.4));
  look.set(0,ly,0);cam.lookAt(look);
  return az;
}
// semillas 2D de cierre
const sem=document.getElementById('sem').getContext('2d');
function drawSeedsEnd(k){
  sem.clearRect(0,0,W,H);
  const N=700,cx=520,cy=1010,R=300,c=R/Math.sqrt(N);const a=(180-137.5)*Math.PI/180,Nn=[-Math.sin(a),-Math.cos(a)],hh=R*0.64;
  const shown=Math.floor(N*(1-Math.pow(1-k,2)));
  const mix=(A,B,t)=>{const p=h=>[1,3,5].map(i=>parseInt(h.substr(i,2),16));const a=p(A),b=p(B);return '#'+a.map((v,i)=>Math.round(v+(b[i]-v)*t).toString(16).padStart(2,'0')).join('')};
  for(let n=1;n<=shown;n++){const r=c*Math.sqrt(n),th=n*GA,x=cx+r*Math.cos(th),y=cy+r*Math.sin(th);if(((x-cx)*Nn[0]+(y-cy)*Nn[1])>hh)continue;
    const tt=n/N;const colr=tt<0.62?mix('#1F1D1A','#2C6D3F',Math.min(1,tt*1.6)):mix('#2C6D3F','#7CC090',(tt-0.62)/0.38);
    sem.globalAlpha=0.9;sem.fillStyle=colr;sem.beginPath();sem.arc(x,y,c*(0.40+0.10*Math.sqrt(n/N)),0,Math.PI*2);sem.fill();}
}
const fin=document.getElementById('fin'),logo=document.getElementById('logo'),es=document.getElementById('es');
window.TOTAL=TOTAL;window.FPS=FPS;
window.renderFrame=function(t){
  const az=setCamera(t);
  // diorama aparece
  const up=ease(seg(t,0,0.9));dio.position.y=-1.6*(1-up);dio.scale.setScalar(0.6+0.4*up);
  // bolas blancas
  whites.forEach((m,i)=>{
    const s=back(seg(t,0.5+i*0.07,1.1+i*0.07));
    let sc=s, op=1, y=m.userData.r*s;
    if(nullified.includes(m.userData.k)){
      const f=ease(seg(t,5.7,6.4)); op=1-0.75*f; sc*= (1-0.55*f);
      m.material.color.setHex(0xFFFFFF).lerp(new THREE.Color(0x9AA7A0),f);
    }
    const out=ease(seg(t,11.0+i*0.05,12.2+i*0.05)); sc*=1-out; op*= (1-out);
    m.scale.setScalar(Math.max(0.0001,sc));m.position.y=m.userData.r*Math.max(0.0001,sc);m.material.opacity=Math.max(0,op);
  });
  slotBlack.visible=t>0.8;
  // bola negra: cae, anula, espera, rueda al centro y se hace semilla
  const dropT=seg(t,4.5,5.6);
  const bp=slotPos(kBlack);
  let by=0.29+ (1-dropT*dropT)*3.6; // caída
  if(dropT<1){ }else{ const bounce=Math.abs(Math.sin(seg(t,5.6,6.3)*Math.PI*1.5))*0.35*(1-seg(t,5.6,6.3)); by=0.29+bounce; }
  const toC=easeIO(seg(t,10.3,11.2));
  const seedR=CS*0.42;
  black.visible=t>4.5;
  black.position.set(bp.x*(1-toC),by*(1-toC)+seedR*toC,bp.z*(1-toC));
  const bs=1-toC*(1-seedR/0.29);black.scale.setScalar(bs);
  black.material.color.setHex(INK).lerp(new THREE.Color(GREEN),toC);
  // semillas
  seeds.forEach(m=>{const a=11.2+ (m.userData.n/NS)*3.0;const s=back(seg(t,a,a+0.5));m.scale.setScalar(Math.max(0.0001,s));m.position.y=m.userData.rad*Math.max(0.0001,s);});
  // carteles: aparecen con escala vertical y miran a cámara
  for(const [k,[a,b]] of Object.entries(window_)){
    const s=signs[k];const inn=back(seg(t,a,a+0.5)),outt=ease(seg(t,b-0.4,b));
    const v=inn*(1-outt);s.visible=v>0.01;
    s.position.set(0,0,0);
    s.scale.set(1,Math.max(0.001,v),1);
    s.rotation.y=az; // enfrentado a la cámara
  }
  // fondo/ cierre
  const f=ease(seg(t,16.2,16.8));fin.style.opacity=f;
  logo.style.opacity=ease((t-16.8)/0.6);
  const e=ease((t-17.2)/0.6);es.style.opacity=e;es.style.transform=`translateY(${(1-e)*14}px)`;
  drawSeedsEnd(clamp((t-16.3)/1.3));
  renderer.render(scene,cam);
};
window.renderFrame(0);window.READY=true;
