package main

import (
	"bufio"
	"fmt"
	"os"
)

func readCli() string {
	reader := bufio.NewReader(os.Stdin)
	cadena, err := reader.ReadString('\n')
	if err != nil {
		return ""
	} else {
		return cadena
	}
}

func count_lines(cadena string) int {
	chain := []rune(cadena)
	return len(chain)
}

func main() {
	var frase string
	fmt.Println("Este programa cuenta los caracteres, de una cadena de caracteres, incluyendo espacios")
	fmt.Print("Introduce una cadena de caracteres, el salto de linea finaliza la entrada de caracteres: ")
	frase = readCli()
	fmt.Printf("La cadena introducida posee: %d caracteres", count_lines(frase))

}
