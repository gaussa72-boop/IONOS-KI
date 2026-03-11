// meta_geometry.js — Sacred Geometry (Lebensblume)
class SacredGeometry {
  constructor() {
    this.canvas = document.getElementById('sacred-geometry-canvas');
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.resize();
    window.addEventListener('resize', () => this.resize());
    this.time = 0;
    requestAnimationFrame(() => this.animate());
  }

  resize() {
    this.width = this.canvas.width = this.canvas.offsetWidth;
    this.height = this.canvas.height = this.canvas.offsetHeight;
    this.cx = this.width / 2; this.cy = this.height / 2;
  }

  drawRing(x, y, r, alpha = 0.3) {
    this.ctx.strokeStyle = `rgba(255,215,0,${alpha})`;
    this.ctx.lineWidth = 1.5; this.ctx.beginPath(); this.ctx.arc(x, y, r, 0, Math.PI * 2); this.ctx.stroke();
  }

  draw() {
    const mainR = 120; const petals = 6;
    this.drawRing(this.cx, this.cy, 30, 0.5);
    for (let i = 0; i < petals; i++) {
      const a = (i / petals) * Math.PI * 2;
      const x = this.cx + Math.cos(a) * mainR;
      const y = this.cy + Math.sin(a) * mainR;
      this.drawRing(x, y, mainR, 0.2);
    }
    const outer = 180;
    for (let i = 0; i < 12; i++) {
      const a = (i / 12) * Math.PI * 2;
      const x = this.cx + Math.cos(a) * outer;
      const y = this.cy + Math.sin(a) * outer;
      this.drawRing(x, y, 40, 0.12);
    }
    const pulse = 60 + Math.sin(this.time * 0.005) * 10;
    this.ctx.strokeStyle = `rgba(0,255,127,${0.4 + Math.sin(this.time * 0.003) * 0.2})`;
    this.ctx.lineWidth = 2;
    this.ctx.beginPath(); this.ctx.arc(this.cx, this.cy, pulse, 0, Math.PI * 2); this.ctx.stroke();
  }

  animate() {
    if (!this.ctx) return; this.ctx.clearRect(0, 0, this.width, this.height); this.draw(); this.time++; requestAnimationFrame(() => this.animate());
  }
}

window.addEventListener('DOMContentLoaded', () => {
  new SacredGeometry();
});

