# [IA] Codex (OpenAI) - rascunhos ilustrativos, sem dados reais.
# Autoria: Codex (OpenAI), solicitado por Adrian Michael em 2026-11-03.
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

function Draw-Text($text, $x, $y, $size = 17, $color = '#334155') {
    $font = [System.Drawing.Font]::new('Segoe UI', $size)
    $brush = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml($color))
    try { $script:canvas.DrawString($text, $font, $brush, [float]$x, [float]$y) }
    finally { $font.Dispose(); $brush.Dispose() }
}

function Draw-Box($x, $y, $w, $h, $fill = '#FFFFFF', $border = '#CBD5E1') {
    $brush = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml($fill))
    $pen = [System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml($border), 1)
    try {
        $script:canvas.FillRectangle($brush, $x, $y, $w, $h)
        $script:canvas.DrawRectangle($pen, $x, $y, $w, $h)
    } finally { $brush.Dispose(); $pen.Dispose() }
}

function Draw-Histogram($x, $y, $w, $h, $title) {
    Draw-Box $x $y $w $h
    Draw-Text $title ($x + 16) ($y + 12) 15
    $heights = @(25, 50, 85, 110, 90, 60, 30)
    for ($i = 0; $i -lt $heights.Count; $i++) {
        Draw-Box ($x + 28 + $i * 37) ($y + $h - 28 - $heights[$i]) 31 $heights[$i] '#93C5FD' '#60A5FA'
    }
    Draw-Text 'frequencia / valores da variavel' ($x + 18) ($y + $h - 25) 10
}

foreach ($dashboard in @(1, 2)) {
    $bitmap = [System.Drawing.Bitmap]::new(1500, 1180)
    $script:canvas = [System.Drawing.Graphics]::FromImage($bitmap)
    try {
        $script:canvas.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
        $script:canvas.Clear([System.Drawing.ColorTranslator]::FromHtml('#F8FAFC'))
        Draw-Text "COLLEGE / RASCUNHO DO DASHBOARD $dashboard" 32 18 23 '#0F172A'
        Draw-Text 'Revisao do planejamento | 2026-11-03 | Codex (OpenAI), a pedido de Adrian Michael' 32 62 14
        Draw-Text 'Esquema de layout posterior ao app inicial. Formas ilustrativas; sem dados calculados.' 32 91 13
        Draw-Box 30 140 275 950 '#EFF6FF'
        Draw-Text 'FILTROS COMPARTILHADOS' 46 160 14 '#1D4ED8'
        Draw-Text 'Variaveis quantitativas' 46 207 15
        Draw-Box 46 245 240 90
        Draw-Text "Apps / Accept / Enroll`nExpend / Grad.Rate`n17 variaveis disponiveis" 57 250 13
        Draw-Text 'Tipo: Todos / No / Yes' 46 343 13
        Draw-Text '[ ] Distinguir por tipo' 46 374 13
        Draw-Text 'Intervalos inclusivos' 46 415 15
        $labels = @('Apps: candidaturas', 'Accept: aceitacoes', 'Enroll: matriculados', 'Expend: gasto por aluno', 'Grad.Rate: graduacao (%)')
        for ($i = 0; $i -lt $labels.Count; $i++) {
            $top = 460 + $i * 83
            Draw-Text $labels[$i] 46 $top 13
            Draw-Box 60 ($top + 38) 205 4 '#94A3B8'
            Draw-Box 60 ($top + 31) 12 18 '#2563EB'
            Draw-Box 253 ($top + 31) 12 18 '#2563EB'
        }
        Draw-Text "Retirar variavel remove`nseu filtro de intervalo.`nFiltros afetam as duas abas." 46 919 12
        $firstFill = '#FFFFFF'; $secondFill = '#FFFFFF'
        if ($dashboard -eq 1) { $firstFill = '#DBEAFE' } else { $secondFill = '#DBEAFE' }
        Draw-Box 330 140 290 48 $firstFill
        Draw-Text '1. Laboratorio' 347 150 17
        Draw-Box 635 140 345 48 $secondFill
        Draw-Text '2. Comparacao institucional' 652 150 15
        Draw-Text 'N filtrados / N da base | mesma amostra nas duas abas' 335 205 14
        if ($dashboard -eq 1) {
            Draw-Box 330 250 425 440
            Draw-Text 'Correlacao selecionavel' 350 269 19
            Draw-Text 'Variaveis selecionadas | escala -1 a 1' 350 308 12
            $palette = @('#1D4ED8', '#93C5FD', '#E2E8F0', '#FDA4AF', '#BE123C')
            for ($row = 0; $row -lt 5; $row++) {
                for ($column = 0; $column -lt 5; $column++) {
                    $color = $palette[[Math]::Abs($row - $column)]
                    Draw-Box (370 + $column * 61) (353 + $row * 51) 58 48 $color
                }
            }
            Draw-Text "Spearman / Pearson / Kendall`nPadrao: Spearman" 350 622 12
            Draw-Histogram 780 250 330 235 'Candidaturas (Apps)'
            Draw-Histogram 1130 250 330 235 'Aceitacoes (Accept)'
            Draw-Histogram 780 505 330 235 'Matriculados (Enroll)'
            Draw-Histogram 1130 505 330 235 'Gasto por aluno (Expend)'
            Draw-Histogram 780 760 330 235 'Graduacao (%)'
            Draw-Text "Um histograma por variavel`nselecionada. Cor por tipo`nquando o toggle esta ligado." 1137 790 14
            Draw-Box 330 1015 1130 75 '#FFF7ED'
            Draw-Text 'Estados vazios: orientar selecao; avisar quando faltarem registros para correlacao.' 347 1036 14
        } else {
            Draw-Text 'Publico de trabalho: planejamento institucional' 335 244 19 '#0F172A'
            Draw-Text 'Revisao individual do publico e das metricas pendente. Dados historicos.' 335 281 14
            $kpis = @("Candidaturas`nmedia de Apps", "Aceitacoes`nmedia de Accept", "Matriculados`nmedia de Enroll", "Gasto por aluno`nmedia de Expend", "Graduacao`nmedia de Grad.Rate")
            for ($i = 0; $i -lt 5; $i++) {
                Draw-Box (330 + $i * 229) 333 214 124
                Draw-Text $kpis[$i] (344 + $i * 229) 351 14
                Draw-Text 'delta vs base' (344 + $i * 229) 422 11
            }
            Draw-Box 330 490 540 285
            Draw-Text '1. Media por tipo [seletor]' 350 505 17
            Draw-Box 410 598 120 130 '#93C5FD'
            Draw-Box 620 628 120 100 '#C4B5FD'
            Draw-Text 'Nao privada' 413 738 12
            Draw-Text 'Privada' 635 738 12
            Draw-Box 895 490 565 285
            Draw-Text '2. Apps x Accept (dispersao)' 913 505 17
            for ($i = 0; $i -lt 12; $i++) {
                Draw-Box (955 + $i * 35) (710 - $i * 11 + ($i % 3) * 12) 9 9 '#C4B5FD'
            }
            Draw-Text 'Candidaturas recebidas / aceitas | cor por tipo' 913 741 12
            Draw-Box 330 798 1130 216
            Draw-Text '3. Distribuicao do gasto por aluno, por tipo (boxplot)' 350 813 17
            Draw-Text 'Nao privada' 355 869 13
            Draw-Text 'Privada' 355 945 13
            Draw-Box 550 865 640 3 '#64748B'
            Draw-Box 745 846 190 43 '#BFDBFE'
            Draw-Box 833 846 3 43 '#1D4ED8'
            Draw-Box 590 940 700 3 '#64748B'
            Draw-Box 790 921 230 43 '#DDD6FE'
            Draw-Box 898 921 3 43 '#7C3AED'
            Draw-Text 'Expend (valor original)' 1165 982 12
            Draw-Box 330 1030 1130 60 '#FFF7ED'
            Draw-Text 'Medias simples entre instituicoes; sem ponderacao por alunos. Deltas comparados a base completa.' 346 1048 13
        }
        Draw-Text 'Fonte planejada: data/clean/dataset.csv | Referencia: entregas/planejamento.md | Sem amostra: exibir aviso' 32 1120 13
        $outputPath = Join-Path $PSScriptRoot "rascunho_dashboard$dashboard.png"
        $bitmap.Save($outputPath, [System.Drawing.Imaging.ImageFormat]::Png)
        Write-Output "Gerado: $outputPath"
    } finally { $script:canvas.Dispose(); $bitmap.Dispose() }
}
