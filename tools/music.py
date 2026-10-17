import numpy as np, wave, sys
SR=44100; BPM=88; beat=60/BPM; dur=float(sys.argv[1]) if len(sys.argv)>1 else 21.0
N=int(SR*dur); out=np.zeros((N,2))
def note(f): return 440*2**((f-69)/12)
def add(sig,start,pan=0.5):
    i=int(start*SR); j=min(N,i+len(sig))
    if i>=N: return
    s=sig[:j-i]; out[i:j,0]+=s*(1-pan); out[i:j,1]+=s*pan
def keys(m,l):  # soft e-piano: few harmonics, exp decay
    t=np.arange(int(l*SR))/SR; f=note(m)
    s=(np.sin(2*np.pi*f*t)+0.35*np.sin(2*np.pi*2*f*t)+0.12*np.sin(2*np.pi*3*f*t))*np.exp(-t*2.2)
    s*=np.minimum(1,t/0.01); return s*0.11
def bass(m,l):
    t=np.arange(int(l*SR))/SR; f=note(m)
    s=np.sin(2*np.pi*f*t)*np.exp(-t*1.5)*np.minimum(1,t/0.02); return s*0.22
def kick():
    t=np.arange(int(0.25*SR))/SR; f=120*np.exp(-t*25)+45
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*14)*0.35
def hat():
    t=np.arange(int(0.05*SR))/SR; n=np.random.default_rng(1).standard_normal(len(t))
    n=np.diff(n,prepend=0); return n*np.exp(-t*90)*0.05
prog=[[60,64,67,71],[57,60,64,67],[53,57,60,64],[55,59,62,65]]  # Cmaj7 Am7 Fmaj7 G7
roots=[36,33,29,31]
bar=4*beat; t0=0; k=0
while t0<dur:
    ch=prog[k%4]
    for b in range(4):
        tb=t0+b*beat
        for n_,m in enumerate(ch): add(keys(m,bar),tb+n_*0.015,0.35+0.1*n_) if b in (0,2) else None
        add(keys(ch[(b+1)%4]+12,beat*1.5),tb+beat*0.5,0.7)
        if b in (0,2): add(kick(),tb)
        add(hat(),tb+beat*0.5,0.6); add(hat(),tb,0.4)
    add(bass(roots[k%4],bar*0.5),t0); add(bass(roots[k%4]+7,bar*0.5),t0+bar*0.5)
    t0+=bar; k+=1
# lowpass-ish smoothing and fades
for c in range(2):
    x=out[:,c]; y=np.copy(x)
    for i in range(1,N): y[i]=y[i-1]+0.35*(x[i]-y[i-1])
    out[:,c]=y
fi=int(0.8*SR); fo=int(1.5*SR)
out[:fi]*=np.linspace(0,1,fi)[:,None]; out[-fo:]*=np.linspace(1,0,fo)[:,None]
out/=np.max(np.abs(out))*1.12
with wave.open('bgm.wav','wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out*32767).astype('<i2').tobytes())
