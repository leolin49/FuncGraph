package main

import (
	"fmt"
	"sort"
)

var (
	g                [][]int
	over             bool
	n, a, b          int
	centerX, centerY int
	dir              = [8][2]int{{-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}, {1, 2}, {2, 1}, {2, -1}, {1, -2}}
)

type Node struct {
	x, y int
	c    int
	d    int
}

type NodeSlice []Node

func (s NodeSlice) Less(i, j int) bool {
	if s[i].c == s[j].c {
		return s[i].d > s[j].d
	}
	return s[i].c < s[j].c
}

func (s NodeSlice) Len() int {
	return len(s)
}

func (s NodeSlice) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func pringG() {
	for _, arr := range g {
		for _, x := range arr {
			fmt.Printf("%d ", x)
		}
		fmt.Print("\n")
	}
}

func ok(x, y int) bool {
	return !(x < 0 || x >= n || y < 0 || y >= n)
}

func cntNext(x, y int) (cnt int) {
	for i := range dir {
		nextX, nextY := x+dir[i][0], y+dir[i][1]
		if ok(nextX, nextY) && g[nextX][nextY] == 0 {
			cnt++
		}
	}
	return
}

func getDis(x, y int) int {
	return abs(x-centerX) + abs(y-centerY)
}

func backtrack(x, y int, step int) {
	if step == n*n {
		if (abs(x-centerX) == 1 && abs(y-centerY) == 2) || (abs(x-centerX) == 2 && abs(y-centerY) == 1) {
			over = true
		}
		return
	}
	q := make(NodeSlice, 0)
	for i := range dir {
		nextX, nextY := x+dir[i][0], y+dir[i][1]
		if ok(nextX, nextY) && g[nextX][nextY] == 0 {
			node := Node{
				x: nextX,
				y: nextY,
				c: cntNext(nextX, nextY),
				d: getDis(nextX, nextY),
			}
			q = append(q, node)
		}
	}
	sort.Sort(q)
	for _, node := range q {
		g[node.x][node.y] = step + 1
		backtrack(node.x, node.y, step+1)
		if over {
			return
		}
		g[node.x][node.y] = 0
	}
}

func main() {
	over = false
	fmt.Scanln(&n, &a, &b)
	centerX, centerY = n/2, n/2
	g = make([][]int, n)
	for i := range g {
		g[i] = make([]int, n)
	}
	g[centerX][centerY] = 1
	backtrack(centerX, centerY, 1)
	// offset
	offset := g[a-1][b-1] - 1
	for i := range g {
		for j := range g[i] {
			if g[i][j] > offset {
				g[i][j] -= offset
			} else {
				g[i][j] += n*n - offset
			}
		}
	}
	pringG()
	return
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
