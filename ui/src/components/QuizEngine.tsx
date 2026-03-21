/* ─── Quiz Engine Component — Annals of the World ─── */
import React, { useState, useCallback } from 'react'
import { Box, Text, Flex, Heading, SimpleGrid } from '@chakra-ui/react'
import { CheckCircle, XCircle, Trophy, RotateCcw, Timer, BookOpen } from 'lucide-react'
import type { QuizSession, QuizResult } from '../types'

interface QuizEngineProps {
  session: QuizSession
  onComplete?: (result: QuizResult) => void
}

export default function QuizEngine({ session, onComplete }: QuizEngineProps) {
  const [currentIndex, setCurrentIndex] = useState(0)
  const [selectedOption, setSelectedOption] = useState<number | null>(null)
  const [showExplanation, setShowExplanation] = useState(false)
  const [answers, setAnswers] = useState<{ questionId: string; selectedIndex: number; correct: boolean }[]>([])
  const [completed, setCompleted] = useState(false)

  const question = session.questions[currentIndex]
  const progress = ((currentIndex) / session.questions.length) * 100

  const difficultyColors: Record<string, string> = {
    beginner: '#38A169', intermediate: '#DD6B20', advanced: '#C53030', expert: '#6B3FA0',
  }

  const handleSelect = useCallback((optionIndex: number) => {
    if (showExplanation) return
    setSelectedOption(optionIndex)
    setShowExplanation(true)

    const correct = optionIndex === question.correctIndex
    setAnswers(prev => [...prev, { questionId: question.id, selectedIndex: optionIndex, correct }])
  }, [showExplanation, question])

  const handleNext = useCallback(() => {
    if (currentIndex < session.questions.length - 1) {
      setCurrentIndex(prev => prev + 1)
      setSelectedOption(null)
      setShowExplanation(false)
    } else {
      setCompleted(true)
      const result: QuizResult = {
        sessionId: session.id,
        score: answers.filter(a => a.correct).length + (selectedOption === question.correctIndex ? 1 : 0),
        total: session.questions.length,
        answers: [...answers],
        completedAt: new Date(),
      }
      onComplete?.(result)
    }
  }, [currentIndex, session, answers, selectedOption, question, onComplete])

  const handleRestart = useCallback(() => {
    setCurrentIndex(0)
    setSelectedOption(null)
    setShowExplanation(false)
    setAnswers([])
    setCompleted(false)
  }, [])

  if (completed) {
    const score = answers.filter(a => a.correct).length
    const percentage = Math.round((score / session.questions.length) * 100)
    const grade = percentage >= 90 ? 'Excellent!' : percentage >= 70 ? 'Well Done!' : percentage >= 50 ? 'Good Effort!' : 'Keep Learning!'

    return (
      <Box bg="white" border="1px solid" borderColor="#E4E2DC" borderRadius="xl" p={8} textAlign="center">
        <Box mx="auto" mb={4} w="60px" h="60px" borderRadius="full" bg={percentage >= 70 ? '#38A16920' : '#DD6B2020'} display="flex" alignItems="center" justifyContent="center">
          <Trophy size={30} color={percentage >= 70 ? '#38A169' : '#DD6B20'} />
        </Box>
        <Heading fontFamily='"Cinzel", serif' fontSize="2xl" color="#2D2A24" mb={2}>{grade}</Heading>
        <Text fontFamily='"Cinzel", serif' fontSize="4xl" fontWeight={700} color="#D4AF37">{score}/{session.questions.length}</Text>
        <Text fontSize="sm" color="#9E9A90" mt={1}>{percentage}% correct</Text>

        <Box h="6px" bg="#F5F4F0" borderRadius="full" mt={6} mb={4} overflow="hidden">
          <Box h="100%" bg={percentage >= 70 ? '#38A169' : '#DD6B20'} borderRadius="full" w={`${percentage}%`} transition="width 1s ease" />
        </Box>

        <SimpleGrid columns={2} gap={4} mt={6}>
          {answers.map((a, i) => (
            <Flex key={i} align="center" gap={2} p={2} bg={a.correct ? '#38A16910' : '#C5303010'} borderRadius="md">
              {a.correct ? <CheckCircle size={14} color="#38A169" /> : <XCircle size={14} color="#C53030" />}
              <Text fontSize="xs" color="#2D2A24" flex={1} textAlign="left">
                Q{i + 1}: {session.questions[i].question.slice(0, 40)}…
              </Text>
            </Flex>
          ))}
        </SimpleGrid>

        <Flex justify="center" gap={4} mt={6}>
          <Box
            as="button" bg="#2D2A24" color="#D4AF37" px={6} py={3} borderRadius="lg"
            cursor="pointer" display="flex" alignItems="center" gap={2}
            _hover={{ bg: '#524E44' }} onClick={handleRestart}
          >
            <RotateCcw size={16} /> Try Again
          </Box>
        </Flex>
      </Box>
    )
  }

  return (
    <Box>
      {/* Progress bar */}
      <Flex align="center" gap={3} mb={4}>
        <Timer size={16} color="#9E9A90" />
        <Box flex={1} h="6px" bg="#F5F4F0" borderRadius="full" overflow="hidden">
          <Box h="100%" bg="#D4AF37" borderRadius="full" w={`${progress}%`} transition="width 0.3s ease" />
        </Box>
        <Text fontSize="xs" color="#9E9A90" fontWeight={600}>{currentIndex + 1}/{session.questions.length}</Text>
      </Flex>

      {/* Difficulty badge */}
      <Flex gap={2} mb={3}>
        <Text fontSize="xs" color="white" bg={difficultyColors[question.difficulty]} px={2.5} py={0.5} borderRadius="full" fontWeight={600}>
          {question.difficulty.charAt(0).toUpperCase() + question.difficulty.slice(1)}
        </Text>
        <Text fontSize="xs" color="#9E9A90" bg="#F5F4F0" px={2.5} py={0.5} borderRadius="full">
          {question.category}
        </Text>
        {question.era && (
          <Text fontSize="xs" color="#9E9A90" bg="#F5F4F0" px={2.5} py={0.5} borderRadius="full">
            {question.era}
          </Text>
        )}
      </Flex>

      {/* Question */}
      <Box bg="white" border="1px solid" borderColor="#E4E2DC" borderRadius="xl" p={6} mb={4}>
        <Flex align="center" gap={2} mb={3}>
          <BookOpen size={18} color="#D4AF37" />
          <Text fontSize="xs" color="#96770B" fontWeight={600}>Question {currentIndex + 1}</Text>
        </Flex>
        <Text fontFamily='"Cormorant Garamond", serif' fontSize="xl" fontWeight={600} color="#2D2A24" lineHeight={1.4}>
          {question.question}
        </Text>
      </Box>

      {/* Options */}
      <SimpleGrid columns={1} gap={3}>
        {question.options.map((option, i) => {
          const isSelected = selectedOption === i
          const isCorrect = i === question.correctIndex
          const showResult = showExplanation

          let bg = 'white'
          let borderColor = '#E4E2DC'
          let textColor = '#2D2A24'

          if (showResult && isCorrect) {
            bg = '#38A16915'; borderColor = '#38A169'; textColor = '#276749'
          } else if (showResult && isSelected && !isCorrect) {
            bg = '#C5303015'; borderColor = '#C53030'; textColor = '#9B2C2C'
          } else if (isSelected) {
            borderColor = '#D4AF37'
          }

          return (
            <Box
              key={i}
              bg={bg} border="2px solid" borderColor={borderColor} borderRadius="lg"
              p={4} cursor={showExplanation ? 'default' : 'pointer'}
              transition="all 0.2s"
              _hover={!showExplanation ? { borderColor: '#D4AF37', transform: 'translateX(4px)' } : {}}
              onClick={() => handleSelect(i)}
            >
              <Flex align="center" gap={3}>
                <Box
                  w="28px" h="28px" borderRadius="full" border="2px solid"
                  borderColor={showResult && isCorrect ? '#38A169' : showResult && isSelected ? '#C53030' : '#D6D3CC'}
                  display="flex" alignItems="center" justifyContent="center"
                  bg={showResult && isCorrect ? '#38A169' : showResult && isSelected && !isCorrect ? '#C53030' : 'transparent'}
                  flexShrink={0}
                >
                  {showResult && isCorrect && <CheckCircle size={16} color="white" />}
                  {showResult && isSelected && !isCorrect && <XCircle size={16} color="white" />}
                  {!showResult && <Text fontSize="xs" fontWeight={600} color="#9E9A90">{String.fromCharCode(65 + i)}</Text>}
                </Box>
                <Text fontSize="sm" color={textColor} fontWeight={isSelected ? 600 : 400}>{option}</Text>
              </Flex>
            </Box>
          )
        })}
      </SimpleGrid>

      {/* Explanation */}
      {showExplanation && (
        <Box bg="#FAFAF8" border="1px solid" borderColor="#E4E2DC" borderRadius="lg" p={4} mt={4}>
          <Text fontSize="xs" fontWeight={700} color="#96770B" mb={1}>Explanation</Text>
          <Text fontSize="sm" color="#524E44" lineHeight={1.6}>{question.explanation}</Text>
          <Box
            as="button" bg="#2D2A24" color="#D4AF37" px={6} py={2} borderRadius="lg" mt={4}
            cursor="pointer" fontSize="sm" fontWeight={600}
            _hover={{ bg: '#524E44' }} onClick={handleNext}
          >
            {currentIndex < session.questions.length - 1 ? 'Next Question →' : 'See Results'}
          </Box>
        </Box>
      )}
    </Box>
  )
}
