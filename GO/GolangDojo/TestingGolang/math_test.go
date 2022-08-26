package math

import (
	"os"
	"testing"
	"time"
)

/*
	t.Log("Similar to fmt.Println() and concurrently safe")
	t.Fail() // Will show a test case has failed in the results
	t.FailNow() // t.Fail() + safely exit without continuing
	t.Error("t.Log() + t.Fail()")
	t.Fatal("t.Log() + t.FailNow()")
*/

func TestAbs(t *testing.T) {
	// -1, 0, 1
	if Abs(-1) < 0 {
		t.Error("Negative value found in abs() with", -1)
	}
	if Abs(0) < 0 {
		t.Error("Negative value found in abs() with", 1)
	}
	if Abs(1) < 0 {
		t.Error("Negative value found in abs() with", 1)
	}
}

func TestAbsSub(t *testing.T) {
	t.Run("Positive", func(t *testing.T) {
		if Abs(1) < 0 {
			t.Error("Negative value found in abs()")
		}
	})
}

func TestSkip(t *testing.T) {
	if len(os.Getenv("GOPATH")) == 0 {
		t.Skip("Skipping test because GOPATH isn't set")
	}
	// ....
	t.Log("Tested with GOPATH: ", os.Getenv("GOPATH"))
}

/*
func TestCleanup(t *testing.T) {
	t.Cleanup(func() {
		t.Log("Cleanup")
	})
	t.Log("Running some test")
}
*/

func TestParallelOne(t *testing.T) {
	time.Sleep(3 * time.Second)
}

func TestParallelTwo(t *testing.T) {
	time.Sleep(3 * time.Second)
}

func TestParallelThree(t *testing.T) {
	time.Sleep(3 * time.Second)
}
