import sys
# 和《通用故事框架》文档里的总览图（Docs 小部件）同一套坐标：三幕按 25:50:25 分宽，第二幕起伏。
ink, quiet, grid, axis = '#1f1f1f', '#6b6b6b', '#e4e2dc', '#9a978f'
A, B, C, tint = '#2a7ae2', '#e8693a', '#14a874', '#efeeea'
y0, yb, r1, r2 = 104, 282, 302, 319
W, H = 760, 336
b = [199, 517, 676]
xs = [90, 160, 255, 355, 455, 548, 604, 656, 708]
def path(ys): return 'M' + 'L'.join(f'{x} {y}' for x, y in zip(xs, ys))
font = "'Noto Sans CJK SC','PingFang SC','Microsoft YaHei','Source Han Sans SC',sans-serif"
title = '三幕结构固定，第二幕要起伏，角色弧线各不相同'
o = []
o.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{title}" font-family="{font}" font-size="13">')
o.append('<title>三幕总览 · 三幕按 25：50：25 分，第二幕要起伏，通用的张力与三种角色弧线</title>')
o.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff"/>')
o.append(f'<text x="24" y="32" font-size="15" font-weight="600" fill="{ink}">{title}</text>')
o.append(f'<line x1="24" x2="48" y1="56" y2="56" stroke="{axis}" stroke-width="2" stroke-dasharray="5 4"/><text x="56" y="60" font-size="11.5" fill="{ink}">张力（通用）</text>')
for x, col, lab in [(160, A, '高-低-高'), (276, B, '高-稍降-底'), (408, C, '低-稍高-顶')]:
    o.append(f'<line x1="{x}" x2="{x+24}" y1="56" y2="56" stroke="{col}" stroke-width="2.5"/><text x="{x+32}" y="60" font-size="11.5" fill="{ink}">{lab}</text>')
o.append(f'<rect x="638" y="{y0}" width="36" height="{yb-y0}" fill="{tint}"/>')
for x in xs:
    o.append(f'<line x1="{x}" x2="{x}" y1="{y0}" y2="{yb}" stroke="{grid}"/><line x1="{x}" x2="{x}" y1="{yb}" y2="{yb+6}" stroke="{axis}" stroke-width="1.25"/>')
o.append(f'<line x1="24" x2="736" y1="{yb}" y2="{yb}" stroke="{axis}" stroke-width="1.25"/>')
for x in b:
    o.append(f'<line x1="{x}" x2="{x}" y1="76" y2="{yb}" stroke="{axis}" stroke-dasharray="4 4"/>')
for x, lab in [(120, '第一幕 建置 · 25%'), (358, '第二幕 冲击 · 50%'), (597, '第三幕 加码与高潮 · 25%')]:
    o.append(f'<text x="{x}" y="92" text-anchor="middle" font-weight="600" fill="{ink}">{lab}</text>')
o.append(f'<text x="708" y="92" text-anchor="middle" font-size="11.5" fill="{quiet}">结尾</text>')
o.append(f'<path d="{path([262,248,226,212,196,176,150,104,236])}" fill="none" stroke="{axis}" stroke-width="2" stroke-dasharray="5 4" stroke-linejoin="round"/>')
for col, ys in [(A,[130,132,196,150,266,262,260,124,128]),(B,[126,128,160,146,196,222,244,268,268]),(C,[262,258,226,240,204,186,166,112,116])]:
    o.append(f'<path d="{path(ys)}" fill="none" stroke="{col}" stroke-width="2.5" stroke-linejoin="round"/>')
for x, lab in zip(xs, ['初始状态','入局','起伏①','起伏②','第二幕终点','加码','最终选择','高潮','结尾']):
    w = ' font-weight="600"' if lab == '高潮' else ''
    o.append(f'<text x="{x}" y="{r1}" text-anchor="middle" font-size="11.5"{w} fill="{ink}">{lab}</text>')
o.append(f'<text x="455" y="{r2}" text-anchor="middle" font-size="10.5" fill="{quiet}">后接情绪氛围加码戏</text>')
o.append('</svg>')
open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(o) + '\n')
