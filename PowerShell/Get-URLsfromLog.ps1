$data = Get-Content '-.txt'

$data | foreach {
$split = $_.split(" ")
$name=$split[0].Trim()
$url=$split[6].Trim()
$name + $url
}