import math
from decimal import Decimal

def remove_exponent(d):
    return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()

def millify(n, precision=0, drop_nulls=True, suffixes=None):
    if suffixes is None:
        suffixes = ['', 'a,', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
                    'Aa', 'Ab', 'Ac', 'Ad', 'Ae', 'Af', 'Ag', 'Ah', 'Ai', 'Aj', 'Ak', 'Al', 'Am', 'An', 'Ao', 'Ap', 'Aq', 'Ar', 'As', 'At', 'Au', 'Av', 'Aw', 'Ax', 'Ay', 'Az',
                    'Ba', 'Bb', 'Bc', 'Bd', 'Be', 'Bf', 'Bg', 'Bh', 'Bi', 'Bj', 'Bk', 'Bl', 'Bm', 'Bn', 'Bo', 'Bp', 'Bq', 'Br', 'Bs', 'Bt', 'Bu', 'Bv', 'Bw', 'Bx', 'By', 'Bz',
                    'Ca', 'Cb', 'Cc', 'Cd', 'Ce', 'Cf', 'Cg', 'Ch', 'Ci', 'Cj', 'Ck', 'Cl', 'Cm', 'Cn', 'Co', 'Cp', 'Cq', 'Cr', 'Cs', 'Ct', 'Cu', 'Cv', 'Cw', 'Cx', 'Cy', 'Cz',
                    'Da', 'Db', 'Dc', 'Dd', 'De', 'Df', 'Dg', 'Dh', 'Di', 'Dj', 'Dk', 'Dl', 'Dm', 'Dn', 'Do', 'Dp', 'Dq', 'Dr', 'Ds', 'Dt', 'Du', 'Dv', 'Dw', 'Dx', 'Dy', 'Dz',
                    'Ea', 'Eb', 'Ec', 'Ed', 'Ee', 'Ef', 'Eg', 'Eh', 'Ei', 'Ej', 'Ek', 'El', 'Em', 'En', 'Eo', 'Ep', 'Eq', 'Er', 'Es', 'Et', 'Eu', 'Ev', 'Ew', 'Ex', 'Ey', 'Ez',
                    'Fa', 'Fb', 'Fc', 'Fd', 'Fe', 'Ff', 'Fg', 'Fh', 'Fi', 'Fj', 'Fk', 'Fl', 'Fm', 'Fn', 'Fo', 'Fp', 'Fq', 'Fr', 'Fs', 'Ft', 'Fu', 'Fv', 'Fw', 'Fx', 'Fy', 'Fz',
                    'Ga', 'Gb', 'Gc', 'Gd', 'Ge', 'Gf', 'Gg', 'Gh', 'Gi', 'Gj', 'Gk', 'Gl', 'Gm', 'Gn', 'Go', 'Gp', 'Gq', 'Gr', 'Gs', 'Gt', 'Gu', 'Gv', 'Gw', 'Gx', 'Gy', 'Gz',
                    'Ha', 'Hb', 'Hc', 'Hd', 'He', 'Hf', 'Hg', 'Hh', 'Hi', 'Hj', 'Hk', 'Hl', 'Hm', 'Hn', 'Ho', 'Hp', 'Hq', 'Hr', 'Hs', 'Ht', 'Hu', 'Hv', 'Hw', 'Hx', 'Hy', 'Hz',
                    'Ia', 'Ib', 'Ic', 'Id', 'Ie', 'If', 'Ig', 'Ih', 'Ii', 'Ij', 'Ik', 'Il', 'Im', 'In', 'Io', 'Ip', 'Iq', 'Ir', 'Is', 'It', 'Iu', 'Iv', 'Iw', 'Ix', 'Iy', 'Iz',
                    'Ja', 'Jb', 'Jc', 'Jd', 'Je', 'Jf', 'Jg', 'Jh', 'Ji', 'Jj', 'Jk', 'Jl', 'Jm', 'Jn', 'Jo', 'Jp', 'Jq', 'Jr', 'Js', 'Jt', 'Ju', 'Jv', 'Jw', 'Jx', 'Jy', 'Jz',
                    'Ka', 'Kb', 'Kc', 'Kd', 'Ke', 'Kf', 'Kg', 'Kh', 'Ki', 'Kj', 'Kk', 'Kl', 'Km', 'Kn', 'Ko', 'Kp', 'Kq', 'Kr', 'Ks', 'Kt', 'Ku', 'Kv', 'Kw', 'Kx', 'Ky', 'Kz',
                    'La', 'Lb', 'Lc', 'Ld', 'Le', 'Lf', 'Lg', 'Lh', 'Li', 'Lj', 'Lk', 'Ll', 'Lm', 'Ln', 'Lo', 'Lp', 'Lq', 'Lr', 'Ls', 'Lt', 'Lu', 'Lv', 'Lw', 'Lx', 'Ly', 'Lz',
                    'Ma', 'Mb', 'Mc', 'Md', 'Me', 'Mf', 'Mg', 'Mh', 'Mi', 'Mj', 'Mk', 'Ml', 'Mm', 'Mn', 'Mo', 'Mp', 'Mq', 'Mr', 'Ms', 'Mt', 'Mu', 'Mv', 'Mw', 'Mx', 'My', 'Mz',
                    'Na', 'Nb', 'Nc', 'Nd', 'Ne', 'Nf', 'Ng', 'Nh', 'Ni', 'Nj', 'Nk', 'Nl', 'Nm', 'Nn', 'No', 'Np', 'Nq', 'Nr', 'Ns', 'Nt', 'Nu', 'Nv', 'Nw', 'Nx', 'Ny', 'Nz',
                    'Oa', 'Ob', 'Oc', 'Od', 'Oe', 'Of', 'Og', 'Oh', 'Oi', 'Oj', 'Ok', 'Ol', 'Om', 'On', 'Oo', 'Op', 'Oq', 'Or', 'Os', 'Ot', 'Ou', 'Ov', 'Ow', 'Ox', 'Oy', 'Oz',
                    'Pa', 'Pb', 'Pc', 'Pd', 'Pe', 'Pf', 'Pg', 'Ph', 'Pi', 'Pj', 'Pk', 'Pl', 'Pm', 'Pn', 'Po', 'Pp', 'Pq', 'Pr', 'Ps', 'Pt', 'Pu', 'Pv', 'Pw', 'Px', 'Py', 'Pz',
                    'Qa', 'Qb', 'Qc', 'Qd', 'Qe', 'Qf', 'Qg', 'Qh', 'Qi', 'Qj', 'Qk', 'Ql', 'Qm', 'Qn', 'Qo', 'Qp', 'Qq', 'Qr', 'Qs', 'Qt', 'Qu', 'Qv', 'Qw', 'Qx', 'Qy', 'Qz',
                    'Ra', 'Rb', 'Rc', 'Rd', 'Re', 'Rf', 'Rg', 'Rh', 'Ri', 'Rj', 'Rk', 'Rl', 'Rm', 'Rn', 'Ro', 'Rp', 'Rq', 'Rr', 'Rs', 'Rt', 'Ru', 'Rv', 'Rw', 'Rx', 'Ry', 'Rz',
                    'Sa', 'Sb', 'Sc', 'Sd', 'Se', 'Sf', 'Sg', 'Sh', 'Si', 'Sj', 'Sk', 'Sl', 'Sm', 'Sn', 'So', 'Sp', 'Sq', 'Sr', 'Ss', 'St', 'Su', 'Sv', 'Sw', 'Sx', 'Sy', 'Sz',
                    'Ta', 'Tb', 'Tc', 'Td', 'Te', 'Tf', 'Tg', 'Th', 'Ti', 'Tj', 'Tk', 'Tl', 'Tm', 'Tn', 'To', 'Tp', 'Tq', 'Tr', 'Ts', 'Tt', 'Tu', 'Tv', 'Tw', 'Tx', 'Ty', 'Tz',
                    'Ua', 'Ub', 'Uc', 'Ud', 'Ue', 'Uf', 'Ug', 'Uh', 'Ui', 'Uj', 'Uk', 'Ul', 'Um', 'Un', 'Uo', 'Up', 'Uq', 'Ur', 'Us', 'Ut', 'Uu', 'Uv', 'Uw', 'Ux', 'Uy', 'Uz',
                    'Va', 'Vb', 'Vc', 'Vd', 'Ve', 'Vf', 'Vg', 'Vh', 'Vi', 'Vj', 'Vk', 'Vl', 'Vm', 'Vn', 'Vo', 'Vp', 'Vq', 'Vr', 'Vs', 'Vt', 'Vu', 'Vv', 'Vw', 'Vx', 'Vy', 'Vz',
                    'Wa', 'Wb', 'Wc', 'Wd', 'We', 'Wf', 'Wg', 'Wh', 'Wi', 'Wj', 'Wk', 'Wl', 'Wm', 'Wn', 'Wo', 'Wp', 'Wq', 'Wr', 'Ws', 'Wt', 'Wu', 'Wv', 'Ww', 'Wx', 'Wy', 'Wz',
                    'Xa', 'Xb', 'Xc', 'Xd', 'Xe', 'Xf', 'Xg', 'Xh', 'Xi', 'Xj', 'Xk', 'Xl', 'Xm', 'Xn', 'Xo', 'Xp', 'Xq', 'Xr', 'Xs', 'Xt', 'Xu', 'Xv', 'Xw', 'Xx', 'Xy', 'Xz',
                    'Ya', 'Yb', 'Yc', 'Yd', 'Ye', 'Yf', 'Yg', 'Yh', 'Yi', 'Yj', 'Yk', 'Yl', 'Ym', 'Yn', 'Yo', 'Yp', 'Yq', 'Yr', 'Ys', 'Yt', 'Yu', 'Yv', 'Yw', 'Yx', 'Yy', 'Yz',
                    'Za', 'Zb', 'Zc', 'Zd', 'Ze', 'Zf', 'Zg', 'Zh', 'Zi', 'Zj', 'Zk', 'Zl', 'Zm', 'Zn', 'Zo', 'Zp', 'Zq', 'Zr', 'Zs', 'Zt', 'Zu', 'Zv', 'Zw', 'Zx', 'Zy', 'Zz'
]
    
    n = float(n)
    if n == 0:
        return '0'
    
    millidx = max(0, min(len(suffixes) - 1, int(math.floor(math.log10(abs(n)) / 3))))
    result = '{:.{precision}f}'.format(n / 10**(3 * millidx), precision=precision)
    
    if drop_nulls:
        result = remove_exponent(Decimal(result))
    
    return f"{result}{suffixes[millidx]}"
