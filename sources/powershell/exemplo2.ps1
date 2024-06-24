$chaveMalisiosa = "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\EncryptorMalicioso"

if(Test-Path $chaveMalisiosa){
    Write-Host "Removendo $chaveMalisiosa"
    Remove-Item $chaveMalisiosa -Force
    Write-Host "Chave removida"
}else{
    Write-Host "Chave $chaveMalisiosa inexistente"
}