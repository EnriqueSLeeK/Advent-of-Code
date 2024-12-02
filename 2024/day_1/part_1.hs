
import System.IO

main = do
  handler <- openFile "input.txt" ReadMode
  readLines handler

readLines handler = do
  eof <- hIsEOF handler
  if eof
    then return ()
  else do
    line <- hGetLine handler
    putStrLn line
    readLines handler
    
